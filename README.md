# 📚 Documentation Index — Ground Plane Calibration System

## Quick Navigation

### 🚀 Just Getting Started? Start Here:

1. **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** ← 10-minute overview of what's new
2. **[QUICKSTART.md](QUICKSTART.md)** ← 5-minute quick reference
3. **[CONFIG_REFERENCE.md](CONFIG_REFERENCE.md)** ← How to set up config.py

---

## Complete Documentation Structure

### 📖 User Guides

| Document | Purpose | Read Time | Audience |
|----------|---------|-----------|----------|
| [QUICKSTART.md](QUICKSTART.md) | 5-min TL;DR reference | 5 min | Everyone |
| [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) | Complete how-to with troubleshooting | 20 min | End users |
| [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md) | Configuration walkthrough | 10 min | System admins |
| [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) | Feature overview & next steps | 10 min | Project managers |

### 🔧 Technical Guides

| Document | Purpose | Read Time | Audience |
|----------|---------|-----------|----------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design & data flows | 30 min | Developers |
| This file | Documentation map | 5 min | Everyone |

### 💾 Code Files

| File | Status | Purpose |
|------|--------|---------|
| [calibration.py](calibration.py) | 🔄 Enhanced | Core homography engine |
| [calibration_tool.py](calibration_tool.py) | ✨ New | Interactive calibration GUI |
| [detector.py](detector.py) | 🔄 Enhanced | World coordinate computation |
| [main.py](main.py) | 🔄 Enhanced | Recalibration menu & controls |
| [config.py](config.py) | 📝 Update needed | Configuration (WORLD_GRID_W/H) |

---

## Find What You Need

### By Use Case

**"I want to set up the system for the first time"**
1. Read: [QUICKSTART.md](QUICKSTART.md)
2. Follow: [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md)
3. Run: `python calibration_tool.py`

**"I'm getting an error during calibration"**
1. Check: [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) → Troubleshooting
2. Or: [QUICKSTART.md](QUICKSTART.md) → Troubleshooting Tree
3. Run: `python calibration_tool.py --validate`

**"I want to understand how it works"**
1. Read: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) → Technical Highlights
2. Deep dive: [ARCHITECTURE.md](ARCHITECTURE.md)
3. Reference: [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) → How It Works

**"I need to recalibrate during monitoring"**
1. Check: [QUICKSTART.md](QUICKSTART.md) → Keyboard Controls
2. Reference: During monitoring, press `C`

**"I want to integrate this into my code"**
1. Study: [ARCHITECTURE.md](ARCHITECTURE.md)
2. Reference API: [QUICKSTART.md](QUICKSTART.md) → API Cheat Sheet
3. Example: [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) → Using Calibrated Coordinates

### By Experience Level

**Beginner** (Non-technical)
1. [QUICKSTART.md](QUICKSTART.md) - Overview
2. [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md) - Setup guide
3. [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) - Detailed steps

**Intermediate** (Technical user)
1. [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - What's new
2. [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) - Full guide
3. [QUICKSTART.md](QUICKSTART.md) - API reference

**Advanced** (Developer)
1. [ARCHITECTURE.md](ARCHITECTURE.md) - System design
2. Code files: `calibration.py`, `detector.py`
3. [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) - Advanced usage section

---

## Document Summaries

### [QUICKSTART.md](QUICKSTART.md)
**Length:** 2-3 minutes  
**Contains:**
- Problem this solves (before/after comparison)
- What you need (materials checklist)
- 3-step workflow (TL;DR)
- Keyboard controls
- Common issues & fixes
- Data flow diagram
- Troubleshooting tree

**Best for:** Quick answers, keyboard shortcuts, finding fixes

---

### [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md)
**Length:** 20-30 minutes  
**Contains:**
- Complete overview
- How it works (homography math explained simply)
- Why it matters (accuracy comparison)
- Quick start (3 options)
- Detailed step-by-step calibration
- Configuration reference
- Using calibrated coordinates (API examples)
- Troubleshooting (detailed explanations)
- Advanced usage (8-point, multi-camera)
- FAQ (common questions)

**Best for:** Complete understanding, in-depth troubleshooting, best practices

---

### [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md)
**Length:** 10 minutes  
**Contains:**
- Pre-calibration measurement instructions
- Step-by-step config.py setup
- Complete config.py documentation
- Calibration workflow diagram
- Detection output format (before/after)
- Grid cell area explanation
- Coordinate system diagram
- Common config mistakes table
- Setup checklist

**Best for:** Configuration, understanding settings, validation checklist

---

### [ARCHITECTURE.md](ARCHITECTURE.md)
**Length:** 30-40 minutes  
**Contains:**
- System overview diagram
- Module breakdown (each file explained)
- Data flow diagrams (initialization, per-frame, recalibration)
- Transformation math (homography, perspective transforms)
- Configuration dependencies
- Error handling patterns
- Performance characteristics
- Testing checklist
- Future enhancements
- Dependency graph

**Best for:** Developers, deep understanding, integration planning

---

### [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
**Length:** 5-10 minutes  
**Contains:**
- What's been implemented (overview)
- Files created/modified
- Getting started (3 steps)
- Detection data structure
- API quick reference
- Common questions (Q&A)
- Technical highlights
- System architecture diagram
- Key metrics
- Files reference

**Best for:** Project overview, status check, next steps

---

## Keyboard Shortcuts Reference

### During Monitoring

```
Q  → Quit monitoring
C  → Open calibration menu
     ├─ V → Validate current calibration
     ├─ R → Recalibrate
     └─ Q → Return to monitoring
```

---

## File Location Map

```
CrowdMonitor/
├── 📝 CODE FILES (Python)
│   ├── calibration.py           (Core engine)
│   ├── calibration_tool.py      (GUI - standalone)
│   ├── detector.py              (World coordinates)
│   ├── main.py                  (Main loop + recal menu)
│   ├── density.py               (Uses world coords)
1. **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** ← 10-minute overview of what's new
2. **[QUICKSTART.md](QUICKSTART.md)** ← 5-minute quick reference
3. **[CONFIG_REFERENCE.md](CONFIG_REFERENCE.md)** ← How to set up config.py

---

## Complete Documentation Structure

### 📖 User Guides

| Document | Purpose | Read Time | Audience |
|----------|---------|-----------|----------|
| [QUICKSTART.md](QUICKSTART.md) | 5-min TL;DR reference | 5 min | Everyone |
| [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) | Complete how-to with troubleshooting | 20 min | End users |
| [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md) | Configuration walkthrough | 10 min | System admins |
| [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) | Feature overview & next steps | 10 min | Project managers |

### 🔧 Technical Guides

| Document | Purpose | Read Time | Audience |
|----------|---------|-----------|----------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design & data flows | 30 min | Developers |
| This file | Documentation map | 5 min | Everyone |

### 💾 Code Files

| File | Status | Purpose |
|------|--------|---------|
| [calibration.py](calibration.py) | 🔄 Enhanced | Core homography engine |
| [calibration_tool.py](calibration_tool.py) | ✨ New | Interactive calibration GUI |
| [detector.py](detector.py) | 🔄 Enhanced | World coordinate computation |
| [main.py](main.py) | 🔄 Enhanced | Recalibration menu & controls |
| [config.py](config.py) | 📝 Update needed | Configuration (WORLD_GRID_W/H) |

---

## Find What You Need

### By Use Case

**"I want to set up the system for the first time"**
1. Read: [QUICKSTART.md](QUICKSTART.md)
2. Follow: [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md)
3. Run: `python calibration_tool.py`

**"I'm getting an error during calibration"**
1. Check: [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) → Troubleshooting
2. Or: [QUICKSTART.md](QUICKSTART.md) → Troubleshooting Tree
3. Run: `python calibration_tool.py --validate`

**"I want to understand how it works"**
1. Read: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) → Technical Highlights
2. Deep dive: [ARCHITECTURE.md](ARCHITECTURE.md)
3. Reference: [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) → How It Works

**"I need to recalibrate during monitoring"**
1. Check: [QUICKSTART.md](QUICKSTART.md) → Keyboard Controls
2. Reference: During monitoring, press `C`

**"I want to integrate this into my code"**
1. Study: [ARCHITECTURE.md](ARCHITECTURE.md)
2. Reference API: [QUICKSTART.md](QUICKSTART.md) → API Cheat Sheet
3. Example: [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) → Using Calibrated Coordinates

### By Experience Level

**Beginner** (Non-technical)
1. [QUICKSTART.md](QUICKSTART.md) - Overview
2. [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md) - Setup guide
3. [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) - Detailed steps

**Intermediate** (Technical user)
1. [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - What's new
2. [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) - Full guide
3. [QUICKSTART.md](QUICKSTART.md) - API reference

**Advanced** (Developer)
1. [ARCHITECTURE.md](ARCHITECTURE.md) - System design
2. Code files: `calibration.py`, `detector.py`
3. [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) - Advanced usage section

---

## Document Summaries

### [QUICKSTART.md](QUICKSTART.md)
**Length:** 2-3 minutes  
**Contains:**
- Problem this solves (before/after comparison)
- What you need (materials checklist)
- 3-step workflow (TL;DR)
- Keyboard controls
- Common issues & fixes
- Data flow diagram
- Troubleshooting tree

**Best for:** Quick answers, keyboard shortcuts, finding fixes

---

### [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md)
**Length:** 20-30 minutes  
**Contains:**
- Complete overview
- How it works (homography math explained simply)
- Why it matters (accuracy comparison)
- Quick start (3 options)
- Detailed step-by-step calibration
- Configuration reference
- Using calibrated coordinates (API examples)
- Troubleshooting (detailed explanations)
- Advanced usage (8-point, multi-camera)
- FAQ (common questions)

**Best for:** Complete understanding, in-depth troubleshooting, best practices

---

### [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md)
**Length:** 10 minutes  
**Contains:**
- Pre-calibration measurement instructions
- Step-by-step config.py setup
- Complete config.py documentation
- Calibration workflow diagram
- Detection output format (before/after)
- Grid cell area explanation
- Coordinate system diagram
- Common config mistakes table
- Setup checklist

**Best for:** Configuration, understanding settings, validation checklist

---

### [ARCHITECTURE.md](ARCHITECTURE.md)
**Length:** 30-40 minutes  
**Contains:**
- System overview diagram
- Module breakdown (each file explained)
- Data flow diagrams (initialization, per-frame, recalibration)
- Transformation math (homography, perspective transforms)
- Configuration dependencies
- Error handling patterns
- Performance characteristics
- Testing checklist
- Future enhancements
- Dependency graph

**Best for:** Developers, deep understanding, integration planning

---

### [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
**Length:** 5-10 minutes  
**Contains:**
- What's been implemented (overview)
- Files created/modified
- Getting started (3 steps)
- Detection data structure
- API quick reference
- Common questions (Q&A)
- Technical highlights
- System architecture diagram
- Key metrics
- Files reference

**Best for:** Project overview, status check, next steps

---

## Keyboard Shortcuts Reference

### During Monitoring

```
Q  → Quit monitoring
C  → Open calibration menu
     ├─ V → Validate current calibration
     ├─ R → Recalibrate
     └─ Q → Return to monitoring
```

---

## File Location Map

```
CrowdMonitor/
├── 📝 CODE FILES (Python)
│   ├── calibration.py           (Core engine)
│   ├── calibration_tool.py      (GUI - standalone)
│   ├── detector.py              (World coordinates)
│   ├── main.py                  (Main loop + recal menu)
│   ├── density.py               (Uses world coords)
│   ├── config.py                (Settings - EDIT THIS)
│   ├── ui.py                    (Display)
│   ├── alert.py                 (Alerts)
│   ├── logger.py                (Logging)
│   ├── flow.py                  (Flow tracking)
│   └── context_risk.py          (Risk assessment)
│
├── 📚 DOCUMENTATION (Markdown)
│   ├── QUICKSTART.md            (← Start here!)
│   ├── CALIBRATION_GUIDE.md     (Complete guide)
│   ├── CONFIG_REFERENCE.md      (Setup instructions)
│   ├── ARCHITECTURE.md          (Technical deep-dive)
│   ├── IMPLEMENTATION_SUMMARY.md (What's new)
│   └── README.md                (This file)
│
├── 💾 DATA FILES
│   ├── homography.npy           (Auto-created after calibration)
│   ├── crowd_log.csv            (Auto-created when monitoring)
│   ├── yolov8m.pt               (YOLO model)
│   └── snapshots/               (Alert recordings)
│
└── 📊 OTHER
    ├── .gitignore
    └── requirements.txt
```

---

## Quick Command Reference

```bash
# Initial Setup
python calibration_tool.py               # Interactive calibration

# Regular Monitoring
python main.py                           # Start monitoring
# Then press:
# C → Calibration menu
# Q → Quit

# Validation Only
python calibration_tool.py --validate    # Check current cal

# Force Recalibration
python calibration_tool.py --recalibrate # Re-calibrate

# Check Calibration Status
python -c "import calibration; print(calibration.is_calibrated())"
```

---

## Reading Paths by Goal

### Goal: Get the system running in 10 minutes
```
1. CONFIG_REFERENCE.md (Measurement & setup)
2. QUICKSTART.md (3-step workflow)
3. Run: python calibration_tool.py
4. Run: python main.py
```

### Goal: Understand perspective correction
```
1. QUICKSTART.md (TL;DR)
2. CALIBRATION_GUIDE.md (How It Works section)
3. ARCHITECTURE.md (Transformation Math section)
```

### Goal: Debug a calibration problem
```
1. QUICKSTART.md (Troubleshooting Tree)
2. CALIBRATION_GUIDE.md (Troubleshooting section)
3. Run: python calibration_tool.py --validate
```

### Goal: Integrate into my own code
```
1. IMPLEMENTATION_SUMMARY.md (API Quick Reference)
2. ARCHITECTURE.md (Module Breakdown)
3. CALIBRATION_GUIDE.md (Using Calibrated Coordinates)
4. Study: calibration.py functions
```

### Goal: Deploy to production
```
1. IMPLEMENTATION_SUMMARY.md (Full overview)
2. ARCHITECTURE.md (System design)
3. QUICKSTART.md (Testing Checklist)
4. CONFIG_REFERENCE.md (Validation Checklist)
```

---

## Documentation Statistics

| Document | Length | Sections | Code Examples |
|----------|--------|----------|----------------|
| QUICKSTART.md | 2-3 min | 12 | 8 |
| CALIBRATION_GUIDE.md | 20-30 min | 20 | 15 |
| CONFIG_REFERENCE.md | 10 min | 10 | 12 |
| ARCHITECTURE.md | 30-40 min | 15 | 20 |
| IMPLEMENTATION_SUMMARY.md | 5-10 min | 15 | 10 |

**Total reading time for complete understanding:** ~60-90 minutes

---

## Version & Updates

- **Version:** 2.0
- **Release Date:** June 2026
- **Last Updated:** June 16, 2026
- **Status:** Production Ready ✅
- **Python:** 3.7+

---

## Still Lost?

**If you don't know where to start:**
1. Read [QUICKSTART.md](QUICKSTART.md) (5 minutes)
2. Follow [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md) (10 minutes)
3. Run `python calibration_tool.py` (2 minutes)
4. Done! Now start monitoring.

**If you hit an error:**
1. Check [QUICKSTART.md](QUICKSTART.md) → Troubleshooting Tree
2. Or search [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md) → Troubleshooting

**If you want to understand the system:**
1. Read [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) (10 min)
2. Then [ARCHITECTURE.md](ARCHITECTURE.md) (30 min)

---

## Quick Links

- 🚀 **Getting Started:** [QUICKSTART.md](QUICKSTART.md)
- ⚙️ **Configuration:** [CONFIG_REFERENCE.md](CONFIG_REFERENCE.md)
- 📖 **Full Guide:** [CALIBRATION_GUIDE.md](CALIBRATION_GUIDE.md)
- 🏗️ **Architecture:** [ARCHITECTURE.md](ARCHITECTURE.md)
- 📋 **Summary:** [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

---

**Happy calibrating! 🎯**
# Crowd_Monitoring1