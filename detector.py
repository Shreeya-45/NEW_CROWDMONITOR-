# detector.py — YOLO tracking + occlusion-aware count + world coordinate mapping

from ultralytics import YOLO
import calibration
from config import (MODEL_PATH, CONF_THRESHOLD, GRID_ROWS, GRID_COLS,
                    OCCLUSION_CORRECTION, OCCLUSION_GAIN)


def load_model():
    return YOLO(MODEL_PATH)


def compute_overlap_ratio(boxes):
    """
    Fraction of detected boxes whose center falls inside another box.
    High overlap → occlusion → YOLO recall drops (ECD-DSA: ~42% in dense).
    """
    n = len(boxes)
    if n < 2:
        return 0.0
    overlap = 0
    for i, (x1, y1, x2, y2) in enumerate(boxes):
        cx, cy = (x1+x2)/2, (y1+y2)/2
        for j, (ox1, oy1, ox2, oy2) in enumerate(boxes):
            if i == j:
                continue
            if ox1 <= cx <= ox2 and oy1 <= cy <= oy2:
                overlap += 1
                break
    return overlap / n


def run_detection(model, frame, frame_h, frame_w):
    """
    Run YOLOv8 tracking, return:
        detections  — list of dicts with keys: x1 y1 x2 y2 cx cy wx wy row col pid
        raw_count   — detections before occlusion correction
        corr_count  — occlusion-corrected float count
        overlap_r   — overlap ratio (0–1)
        zone_counts — 2-D list [GRID_ROWS][GRID_COLS]
    """
    cell_w = frame_w // GRID_COLS
    cell_h = frame_h // GRID_ROWS

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        conf=CONF_THRESHOLD,
        verbose=False
    )

    detections  = []
    zone_counts = [[0]*GRID_COLS for _ in range(GRID_ROWS)]
    boxes_raw   = []

    if results[0].boxes is not None:
        for box in results[0].boxes:
            if model.names[int(box.cls[0])] != "person":
                continue
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = (x1+x2)//2
            cy = (y1+y2)//2
            col = min(cx // cell_w, GRID_COLS-1)
            row = min(cy // cell_h, GRID_ROWS-1)
            pid = int(box.id[0]) if box.id is not None else -1
            zone_counts[row][col] += 1
            boxes_raw.append((x1, y1, x2, y2))
            
            # Compute world coordinates if calibrated
            wx, wy = None, None
            if calibration.is_calibrated():
                try:
                    world_pt = calibration.px_to_world([(cx, cy)])
                    wx, wy = float(world_pt[0, 0]), float(world_pt[0, 1])
                except:
                    wx, wy = None, None
            
            detections.append(dict(x1=x1, y1=y1, x2=x2, y2=y2,
                                   cx=cx, cy=cy, fx=cx, fy=y2,
                                   wx=wx, wy=wy,
                                   row=row, col=col, pid=pid))

    raw_count   = len(detections)
    overlap_r   = compute_overlap_ratio(boxes_raw)
    corr_count  = (raw_count * (1 + OCCLUSION_GAIN * overlap_r)
                   if OCCLUSION_CORRECTION else float(raw_count))

    return detections, raw_count, corr_count, overlap_r, zone_counts