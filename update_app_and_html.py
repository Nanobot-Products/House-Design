# update_app_and_html.py
import re
import os

base_dir = r"C:\Users\vikas\.gemini\antigravity\scratch\house-interior-3d-designer"

# 1. Update js/app.js
app_path = os.path.join(base_dir, "js", "app.js")
with open(app_path, "r", encoding="utf-8") as f:
    app_code = f.read()

# Make 3d_orbit the default view mode
app_code = re.sub(r"this\.viewMode\s*=\s*'2d_plan';", "this.viewMode = '3d_orbit';", app_code)

# Ensure left sidebar starts collapsed and right sidebar starts collapsed in init()
init_hook = """      // Initial render in 3D Orbit view
      this.floorplan2D.render();
      this.scene3D.rebuildScene(this.projectData);
      
      // Auto-collapse sidebars for a clean, spacious 3D viewport
      const leftSb = document.getElementById('left-sidebar');
      if (leftSb) leftSb.classList.add('collapsed');
      const rightSb = document.getElementById('right-sidebar');
      if (rightSb) rightSb.classList.add('collapsed');
      
      this.setViewMode('3d_orbit');
    }"""

app_code = re.sub(
    r"this\.floorplan2D\.render\(\);\s*this\.scene3D\.rebuildScene\(this\.projectData\);\s*}",
    init_hook,
    app_code
)

# In selectObject, auto-open right sidebar if object is selected, or collapse if null
select_hook = """    selectObject(obj) {
      this.selectedObject = obj;
      if (this.floorplan2D) {
        this.floorplan2D.selectedObject = obj;
      }
      const rightSb = document.getElementById('right-sidebar');
      if (rightSb) {
        if (obj) {
          rightSb.classList.remove('collapsed');
        } else {
          rightSb.classList.add('collapsed');
        }
      }
      this.renderInspector();
    }"""

app_code = re.sub(
    r"selectObject\(obj\)\s*\{[\s\S]*?this\.renderInspector\(\);\s*\}",
    select_hook,
    app_code
)

# Add helper methods to App class: toggleLeftSidebar, closeInspector, openRoomSizesModal
extra_methods = """
    toggleLeftSidebar() {
      const sb = document.getElementById('left-sidebar');
      if (sb) {
        sb.classList.toggle('collapsed');
      }
    }

    closeInspector() {
      this.selectObject(null);
      const sb = document.getElementById('right-sidebar');
      if (sb) sb.classList.add('collapsed');
    }

    openRoomSizesModal() {
      const m = document.getElementById('room-sizes-modal');
      if (m) m.classList.add('active');
    }

    closeRoomSizesModal() {
      const m = document.getElementById('room-sizes-modal');
      if (m) m.classList.remove('active');
    }
"""

if "toggleLeftSidebar()" not in app_code:
    app_code = app_code.replace("    setupUI() {", extra_methods + "\n    setupUI() {")

# In setupUI(), add event listeners for new clean UI elements
ui_listeners = """      // Toggle Left Sidebar (Drawer)
      const btnToggleCat = document.getElementById('btn-toggle-catalog');
      if (btnToggleCat) btnToggleCat.addEventListener('click', () => this.toggleLeftSidebar());
      const btnCloseCat = document.getElementById('btn-close-catalog');
      if (btnCloseCat) btnCloseCat.addEventListener('click', () => this.toggleLeftSidebar());

      // Close Right Inspector
      const btnCloseInsp = document.getElementById('btn-close-inspector');
      if (btnCloseInsp) btnCloseInsp.addEventListener('click', () => this.closeInspector());

      // Room Sizes Modal
      const btnRoomSizes = document.getElementById('btn-room-sizes');
      if (btnRoomSizes) btnRoomSizes.addEventListener('click', () => this.openRoomSizesModal());
      const btnCloseRoomSizes = document.getElementById('modal-close-room-sizes');
      if (btnCloseRoomSizes) btnCloseRoomSizes.addEventListener('click', () => this.closeRoomSizesModal());
      const roomSizesModal = document.getElementById('room-sizes-modal');
      if (roomSizesModal) {
        roomSizesModal.addEventListener('click', (e) => {
          if (e.target === roomSizesModal) this.closeRoomSizesModal();
        });
      }
"""

if "btnToggleCat" not in app_code:
    app_code = app_code.replace("    setupUI() {", "    setupUI() {\n" + ui_listeners)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_code)

print("Updated js/app.js successfully!")
