# 🏠 HomeCraft 3D Studio - House & Interior Designer

An interactive, responsive 3D House Blueprint and Interior Design application built with **HTML5, WebGL, and Three.js**. Design floor plans from scratch or use pre-loaded templates, customize walls and rooms, furnish your spaces with a comprehensive 3D interior catalog, and walk through your home in first-person 3D!

---

## 🚀 Quick Start

### Method 1: Using the Python launcher (Recommended)
Open PowerShell or Terminal in this folder and run:
```powershell
python server.py
```
This will automatically launch a local HTTP server and open the app in your default browser at `http://localhost:8080/index.html`.

### Method 2: Direct File Open
You can also directly double-click `index.html` to open the app in any modern web browser (Edge, Chrome, Firefox, Brave).

---

## ✨ Key Features & Controls

### 1. Dual-Mode Design Environment
- **📐 2D Blueprint Mode**:
  - **Wall Tool (`🧱 Wall`)**: Click to start drawing, move mouse to preview dimensions, click to place end point. Continuous wall drawing with snap-to-grid.
  - **Door Tool (`🚪 Door`)**: Hover and click anywhere along a wall to insert an interior door.
  - **Window Tool (`🪟 Window`)**: Hover and click along an exterior or interior wall to place a window.
  - **Select Tool (`👆 Select`)**: Click any furniture, wall, or opening to select it.
    - Drag furniture to move.
    - Drag the top blue rotation circle to rotate in 15° increments.
    - Drag wall endpoint handles to extend or reshape walls.
  - **Pan & Zoom**: Use the mouse wheel to zoom in/out. Right-click + drag or Middle-click + drag to pan the blueprint.

- **🌐 3D Real-Time Orbit View**:
  - Automatically extrudes your 2D walls into 3D meshes with real cutouts for doors and windows.
  - Renders realistic floor textures (Oak Parquet, Dark Walnut, Carrara Marble, Gray Slate Tile, Cozy Carpet).
  - Dynamic sun lighting with soft shadows and time-of-day slider.
  - **Orbit Controls**: Left-click + drag to rotate 360°, right-click + drag to pan, scroll wheel to zoom.
  - Quick camera presets on the bottom bar: **Perspective 3D**, **Bird's Eye Top**, **Front Elevation**, **Side View**.

- **🚶 First-Person Walkthrough Mode**:
  - Puts you directly inside your designed home at natural eye level (1.65m)!
  - **Controls**:
    - <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> or Arrow Keys: Walk around rooms
    - **Mouse**: Look in any direction (360° pan & tilt)
    - <kbd>ESC</kbd>: Exit walkthrough mode and return to 3D orbit

---

### 2. Comprehensive Furniture & Fixture Catalog
Browse categorized items from the left sidebar or use the search bar:
- **🛋️ Living Room**: L-shaped sectional sofa, 3-seater couch, oak coffee table, media console with 65" TV, accent armchair, arc floor lamp (casts real light!), and plush area rug.
- **🛏️ Bedroom**: King size platform bed with headboard and pillows, single bed, bedside nightstand with lamp, 3-door wardrobe with mirror, study desk with laptop.
- **🍳 Kitchen & Dining**: Countertop cabinets, sink unit, double-door refrigerator, kitchen island with bar stools, 6-seater dining set.
- **🚿 Bathroom**: Freestanding bathtub, modern vanity sink with mirror, glass shower cabin, ceramic toilet.
- **🌿 Decor & Lighting**: Potted Monstera plants, framed wall art prints, ceiling fan.

---

### 3. Properties Inspector & Customization
Select any element to customize it in the right sidebar:
- **Furniture**: Change rotation angle, position, color palette (Navy, Emerald, Terracotta, Camel, Charcoal, etc.), duplicate or delete.
- **Walls**: Adjust height and thickness.
- **Rooms**: Rename room, view calculated area in $m^2$ and $sq\ ft$, select flooring finish (Oak, Walnut, Marble, Tile, Carpet).
- **Environment**: Adjust time of day (6:00 to 22:00) to preview morning sun vs sunset vs night lighting, toggle ceiling/roof cover, toggle dimension labels.

---

### 4. Persistence & Export
- **💾 Save**: Exports your entire blueprint and interior layout to a `.json` file.
- **📂 Open**: Loads any previously saved `.json` house design file.
- **📸 Snapshot**: Renders a high-resolution PNG image of your 3D view or 2D floor plan for printing or sharing.
- **📑 Templates**: Instantly switch between **Modern 2BHK Apartment**, **Cozy Urban Studio Loft**, or **Blank Canvas**.

---

## ⌨️ Keyboard Shortcuts Reference
| Shortcut | Action |
|---|---|
| <kbd>R</kbd> | Rotate selected furniture by 45° |
| <kbd>Del</kbd> / <kbd>Backspace</kbd> | Delete selected wall, furniture, or fixture |
| <kbd>Esc</kbd> | Cancel current drawing tool / Deselect / Exit walkthrough |
| <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> | Walk inside the house (Walkthrough mode) |
| <kbd>Ctrl</kbd> + <kbd>Z</kbd> | Undo |
| <kbd>Ctrl</kbd> + <kbd>Y</kbd> | Redo |
