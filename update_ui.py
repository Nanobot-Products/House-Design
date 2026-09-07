# update_ui.py - Updates CSS and JS for ultra-clean, simple, full-screen UI
import os

base_dir = r"C:\Users\vikas\.gemini\antigravity\scratch\house-interior-3d-designer"

# 1. Update css/styles.css with drawer and floating inspector styles
css_append = """
/* ==========================================================================
   ULTRA-CLEAN & SIMPLE UI ENHANCEMENTS
   ========================================================================== */

/* Full-viewport canvas */
#workspace {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

#viewport-container {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

/* Floating Left Drawer for Furniture & Tools */
#left-sidebar {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 320px;
  max-width: 85vw;
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(20px);
  border-right: 1px solid var(--border-color);
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.6);
  z-index: 100;
  transform: translateX(0);
  transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

#left-sidebar.collapsed {
  transform: translateX(-100%);
  pointer-events: none;
}

/* Floating button to open sidebar */
#btn-toggle-catalog {
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 80;
  background: rgba(30, 41, 59, 0.9);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(56, 189, 248, 0.4);
  color: #38bdf8;
  padding: 8px 16px;
  border-radius: 24px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s ease;
}

#btn-toggle-catalog:hover {
  background: #0284c7;
  color: #ffffff;
  border-color: #0284c7;
  transform: translateY(-1px);
}

.drawer-close-btn {
  background: rgba(51, 65, 85, 0.6);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.drawer-close-btn:hover {
  background: #ef4444;
  border-color: #ef4444;
  color: #ffffff;
}

/* Floating Right Inspector Card */
#right-sidebar {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 310px;
  max-width: 90vw;
  max-height: calc(100% - 28px);
  background: rgba(15, 23, 42, 0.94);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
  z-index: 80;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: all 0.24s cubic-bezier(0.16, 1, 0.3, 1);
}

#right-sidebar.collapsed {
  opacity: 0;
  pointer-events: none;
  transform: translateY(-10px) scale(0.96);
}

.inspector-header {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.inspector-close-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 16px;
  line-height: 1;
  padding: 2px 6px;
  border-radius: 4px;
}
.inspector-close-btn:hover {
  color: #fff;
  background: rgba(255,255,255,0.1);
}

/* Floating Camera Presets Bar */
.camera-quick-bar {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(14px);
  border: 1px solid var(--border-color);
  padding: 6px 12px;
  border-radius: 30px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
  z-index: 70;
}

.cam-btn {
  background: rgba(51, 65, 85, 0.6);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease;
}

.cam-btn:hover {
  background: var(--accent-primary);
  border-color: var(--accent-primary);
  color: #ffffff;
}

/* Floating Navigation / Interaction Hint */
.interaction-hint-pill {
  position: absolute;
  bottom: 74px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(15, 23, 42, 0.75);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: var(--text-muted);
  padding: 5px 14px;
  border-radius: 16px;
  font-size: 11px;
  pointer-events: none;
  z-index: 60;
  white-space: nowrap;
}

/* Modal Table Styling for Room Sizes */
.room-size-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 12px;
}

.room-size-table th {
  background: rgba(30, 41, 59, 0.8);
  color: #38bdf8;
  text-align: left;
  padding: 8px 10px;
  border-bottom: 2px solid var(--border-color);
  font-weight: 600;
}

.room-size-table td {
  padding: 8px 10px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  color: var(--text-main);
}

.room-size-table tr:hover {
  background: rgba(51, 65, 85, 0.3);
}

.vastu-tag {
  display: inline-block;
  padding: 2px 7px;
  border-radius: 10px;
  font-size: 10px;
  font-weight: bold;
}
.vastu-tag.sw { background: rgba(244, 63, 94, 0.2); color: #fda4af; }
.vastu-tag.se { background: rgba(245, 158, 11, 0.2); color: #fde68a; }
.vastu-tag.ne { background: rgba(16, 185, 129, 0.2); color: #a7f3d0; }
.vastu-tag.nw { background: rgba(56, 189, 248, 0.2); color: #bae6fd; }
.vastu-tag.cen { background: rgba(168, 85, 247, 0.2); color: #e9d5ff; }
"""

# Append to styles.css
styles_path = os.path.join(base_dir, "css", "styles.css")
with open(styles_path, "r", encoding="utf-8") as f:
    orig_css = f.read()

if "ULTRA-CLEAN & SIMPLE UI ENHANCEMENTS" not in orig_css:
    with open(styles_path, "a", encoding="utf-8") as f:
        f.write("\n" + css_append)
    print("Updated css/styles.css successfully!")
else:
    print("css/styles.css already has enhancements!")
