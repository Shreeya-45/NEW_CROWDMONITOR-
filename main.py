# main.py — Crowd Monitoring System with Live Calibration Support
#
# Key Features:
# • Ground-plane homography calibration with live preview
# • Real-time crowd density with perspective correction
# • Recalibration support (press 'C' during monitoring)
# • Comprehensive logging and alerting
# • Context-aware risk assessment

import cv2
import time
import os

from config import (
    CAMERA_INDEX,
    CAPTURE_W,
    CAPTURE_H,
    DISPLAY_W,
    DISPLAY_H
)

from detector   import load_model, run_detection
from density    import DensityTracker
from flow       import FlowTracker, draw_flow
from cnn_model  import DensityCNN
from alert      import AlertManager
from logger     import init_log, log_frame
from ui         import render_frame, select_place
from context_risk import get_context_risk, get_place
import calibration

from ground_segmentor import GroundSegmentor
from temporal_filter import TemporalFilter
from congestion import CongestionDetector


# ─────────────────────────────────────────────────────────────────────────────
# Calibration management
# ─────────────────────────────────────────────────────────────────────────────

def startup_calibration_check():
    """
    Try to load a saved homography.
    If none exists, offer to calibrate now or fall back to the constant.
    """
    print("\n" + "="*70)
    print("CALIBRATION CHECK")
    print("="*70)
    
    H = calibration.load_homography()

    if H is not None:
        print("✓ Homography loaded — using real-world perspective correction")
        print("  File: calibration.npy")
        print("\n  During monitoring, press 'C' to recalibrate or validate.")
        return True
    
    print("✗ No calibration file found.")
    print("\n  Option 1: Calibrate now (recommended, takes ~2 minutes)")
    print("  Option 2: Continue with fallback constant (less accurate)")
    print("  Option 3: Run calibration_tool.py separately and restart\n")
    
    choice = input("  Enter choice (1/2/3): ").strip()

    if choice == "1":
        print("\nStarting interactive calibration...")
        try:
            if calibration.run_live_calibration_ui():
                print("✓ Calibration successful!")
                return True
            else:
                print("✗ Calibration failed. Using fallback.")
                return False
        except Exception as e:
            print(f"✗ Calibration error: {e}")
            print("✗ Using fallback constant.")
            return False
    elif choice == "3":
        print("\nPlease run: python calibration_tool.py")
        print("Then restart this program.")
        exit(0)
    else:
        print("\n⚠  Using uniform CELL_AREA_M2 constant (fallback)")
        print("  Note: Density may be inaccurate with angled cameras")
        return False


def runtime_recalibration_menu():
    """
    Show menu for recalibration/validation during monitoring.
    """
    print("\n" + "="*70)
    print("CALIBRATION MENU")
    print("="*70)
    
    if calibration.is_calibrated():
        print("Current status: ✓ Calibrated")
        print("Options:")
        print("  [V] Validate current calibration")
        print("  [R] Recalibrate")
        print("  [Q] Return to monitoring")
        choice = input("\nEnter choice (V/R/Q): ").strip().upper()
        
        if choice == "V":
            print("\nValidating calibration...")
            try:
                cap = cv2.VideoCapture(CAMERA_INDEX)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH,  CAPTURE_W)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_H)
                ret, frame = cap.read()
                cap.release()
                
                if ret:
                    if calibration.validate_calibration(test_frame=frame):
                        print("✓ Calibration validation: PASSED")
                    else:
                        print("✗ Calibration validation: REJECTED")
                else:
                    print("✗ Cannot read from camera.")
            except Exception as e:
                print(f"✗ Validation error: {e}")
                
        elif choice == "R":
            print("\nStarting recalibration...")
            if calibration.recalibrate_interactive():
                print("✓ Recalibration successful!")
            else:
                print("✗ Recalibration failed or cancelled.")
    else:
        print("Current status: ✗ Not calibrated (using fallback)")
        print("Options:")
        print("  [C] Calibrate now")
        print("  [Q] Return to monitoring")
        choice = input("\nEnter choice (C/Q): ").strip().upper()
        
        if choice == "C":
            print("\nStarting calibration...")
            try:
                if calibration.run_live_calibration_ui():
                    print("✓ Calibration successful!")
                else:
                    print("✗ Calibration failed.")
            except Exception as e:
                print(f"✗ Calibration error: {e}")
    
    print("\nResuming monitoring...\n")
    time.sleep(1)


# ─────────────────────────────────────────────────────────────────────────────
# Risk colour
# ─────────────────────────────────────────────────────────────────────────────

def get_risk_color(risk):
    return {
        "VERY LOW": (80,  220, 100),
        "LOW":      (0,   220, 255),
        "MODERATE": (0,   200, 255),
        "HIGH":     (0,   140, 255),
        "CRITICAL": (60,  60,  255),
    }.get(risk, (0, 0, 255))


# ─────────────────────────────────────────────────────────────────────────────
# Main loop
# ─────────────────────────────────────────────────────────────────────────────

def main():

    # 1. Calibration
    startup_calibration_check()

    # 2. Select monitoring zone
    select_place()
    print("Selected Place:", get_place())

    use_auto_seg = input("\nDo you want to use AI auto-segmentation for the walkable area? (y/n): ").strip().lower() == 'y'
    segmentor = GroundSegmentor() if use_auto_seg else None

    # 3. Init log file
    init_log()

    # 4. Load YOLO
    model = load_model()

    # 5. Camera
    cap = cv2.VideoCapture(CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  CAPTURE_W)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_H)

    cv2.namedWindow("Crowd Density Monitoring", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Crowd Density Monitoring", DISPLAY_W, DISPLAY_H)

    # 6. Trackers
    density_tracker = DensityTracker()
    flow_tracker    = FlowTracker()
    cnn_model       = DensityCNN() if os.path.exists(os.path.join("models", "crowd_cnn.pt")) else None
    alert_manager   = AlertManager()
    
    # 7. Robustness Filters
    temporal_filter = TemporalFilter()
    congestion_detector = CongestionDetector(
        roi_polygon=None,  # We'll use the default full frame initially
        frame_shape=(CAPTURE_H, CAPTURE_W),
        rows=GRID_ROWS, cols=GRID_COLS
    )

    frame_idx = 0
    prev      = time.time()
    
    print("\n" + "="*70)
    print("MONITORING STARTED")
    print("="*70)
    print("Controls:")
    print("  [Q] Quit")
    print("  [C] Calibration menu (validate/recalibrate)")
    print("="*70 + "\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_idx += 1
        h, w = frame.shape[:2]

        # ── Auto Segmentation (Run once) ──────────────────────────────────
        if frame_idx == 1 and segmentor and segmentor.is_available:
            print("\n[AI] Running ground segmentation on first frame...")
            mask = segmentor.segment(frame)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                pts_px = largest_contour.reshape(-1, 2)
                if calibration.is_calibrated():
                    import config
                    pts_w = calibration.px_to_world(pts_px.tolist())
                    config.MANUAL_ROI = pts_w.tolist()
                    print(f"[AI] Auto-generated monitoring zone with {len(pts_w)} points.")

        # ── Detection ─────────────────────────────────────────────────────
        detections, _, count, overlap, zone_counts = run_detection(
            model, frame, h, w
        )
        
        # ── Temporal Smoothing ────────────────────────────────────────────
        zone_counts_np = np.array(zone_counts, dtype=np.float32)
        smoothed_counts = temporal_filter.update(zone_counts_np)
        
        # ── Cell-Level Congestion Alerts ──────────────────────────────────
        _, cell_alerts = congestion_detector.analyze(detections)

        # ── CNN Density Estimation ────────────────────────────────────────
        cnn_count, cnn_map = 0.0, None
        if cnn_model:
            cnn_count, cnn_map = cnn_model.predict(frame)

        # ── Density (real-world) ───────────────────────────────────────────
        (
            stable_count,
            density,
            phys_density,
            room_density,
            cells,
            hull,
            area,
            kde_map,
            hull_type,
            alpha_value
        ) = density_tracker.update(count, zone_counts, detections, w, h, cnn_count=cnn_count)

        # ── Flow (real-world velocities) ───────────────────────────────────
        vectors, cell_flow = flow_tracker.update(detections)

        # ── Context-aware risk ─────────────────────────────────────────────
        risk  = get_context_risk(stable_count)
        color = get_risk_color(risk)

        # ── FPS ───────────────────────────────────────────────────────────
        now = time.time()
        fps = 1 / max(now - prev, 0.001)
        prev = now

        # ── Alert ─────────────────────────────────────────────────────────
        annotated = frame.copy()    # alert recording uses the annotated frame
        alert_active = alert_manager.update(risk, frame, frame_idx, annotated)

        # ── Logging ───────────────────────────────────────────────────────
        log_frame(frame_idx, stable_count, density, area, risk, overlap, fps)

        # ── Draw flow on frame before render ──────────────────────────────
        draw_flow(frame, vectors, cell_flow, h, w)

        # ── UI render ─────────────────────────────────────────────────────
        output = render_frame(
            frame=frame.copy(),
            detections=detections,
            cell_densities=cells,
            density_history=density_tracker.history(),
            stable_count=stable_count,
            smooth_density=density,
            overlap_ratio=overlap,
            fps=fps,
            risk=risk,
            risk_color=color,
            frame_idx=frame_idx,
            alert_active=alert_active,
            hull_pts=hull,
            hull_area_m2=area,
            zone_counts=smoothed_counts.tolist(), # Use smoothed counts
            kde_map=kde_map,
            phys_density=phys_density,
            room_density=room_density,
            hull_type=hull_type,
            alpha_value=alpha_value,
            cell_alerts=cell_alerts # Pass congestion alerts
        )

        cv2.imshow("Crowd Density Monitoring", output)

        # ── Keyboard input ────────────────────────────────────────────────
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or key == ord("Q"):
            print("\n✓ Shutting down...")
            break
        elif key == ord("c") or key == ord("C"):
            # Pause monitoring for calibration menu
            print("\n[MONITORING] Paused for calibration menu...")
            runtime_recalibration_menu()

    # ── Cleanup ───────────────────────────────────────────────────────────
    alert_manager.release()
    cap.release()
    cv2.destroyAllWindows()
    print("✓ Monitoring stopped.\n")


if __name__ == "__main__":
    main()
