# bundle.py - Generates the complete ultra-clean single-file index.html
import os

base_dir = r"C:\Users\vikas\.gemini\antigravity\scratch\house-interior-3d-designer"

# Read styles.css
with open(os.path.join(base_dir, "css", "styles.css"), "r", encoding="utf-8") as f:
    css_content = f.read()

# Read js files
js_files = [
    "furnitureCatalog.js",
    "templates.js",
    "floorplan2d.js",
    "scene3d.js",
    "app.js"
]

all_js = []
for js_name in js_files:
    with open(os.path.join(base_dir, "js", js_name), "r", encoding="utf-8") as f:
        all_js.append(f"// ==================== {js_name} ====================\n" + f.read())

combined_js = "\n\n".join(all_js)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HomeCraft 3D - 100% Hindu Vastu 30x60 Villa (Jodhpur South-Facing)</title>
  <style>
{css_content}
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header id="top-header">
    <div class="brand-section">
      <div class="brand-icon">🕉️</div>
      <div>
        <span class="brand-title">HomeCraft 3D</span>
        <span class="brand-badge">Jodhpur 30×60 South-Facing</span>
      </div>
    </div>

    <!-- Clean Central View Mode Switcher -->
    <div class="view-modes">
      <button class="mode-btn active" data-mode="3d_orbit" title="360° Interactive 3D Model">
        <span>🌐</span>
        <span>3D View</span>
      </button>
      <button class="mode-btn" data-mode="3d_walk" title="First-Person Walkthrough (WASD)">
        <span>🚶</span>
        <span>Walk Inside</span>
      </button>
      <button class="mode-btn" data-mode="2d_plan" title="Architectural Blueprint Dimensions">
        <span>📐</span>
        <span>2D Blueprint</span>
      </button>
    </div>

    <!-- Header Actions -->
    <div class="header-actions">
      <button class="action-btn" id="btn-room-sizes" title="View Room Sizes & Vastu Guide">
        <span>📏</span>
        <span>Room Sizes</span>
      </button>
      <button class="action-btn" id="btn-snapshot" title="Capture Photo of Current View">
        <span>📸</span>
        <span>Photo</span>
      </button>
      <button class="action-btn primary" id="btn-save-project" title="Save Project Design">
        <span>💾</span>
        <span>Save</span>
      </button>
      <button class="action-btn" id="btn-templates" style="display: none;">📑</button>
      <button class="action-btn" id="btn-load-project" style="display: none;">📂</button>
      <button class="action-btn" id="btn-undo" style="display: none;">↩️</button>
      <button class="action-btn" id="btn-redo" style="display: none;">↪️</button>
      <input type="file" id="file-input-load" accept=".json" style="display: none;">
    </div>
  </header>

  <!-- Multi-Floor Level Switcher & Orientation Bar -->
  <div id="floor-bar">
    <div class="floor-tabs">
      <button class="floor-tab-btn active" data-floor="0">
        <span>🅿️</span>
        <span>Ground Floor</span>
      </button>
      <button class="floor-tab-btn" data-floor="1">
        <span>🏠</span>
        <span>1st Floor (Bro 1)</span>
      </button>
      <button class="floor-tab-btn" data-floor="2">
        <span>🏠</span>
        <span>2nd Floor (Bro 2)</span>
      </button>
      <button class="floor-tab-btn" data-floor="-1" style="border-color: #38bdf8; color: #38bdf8;">
        <span>🏢</span>
        <span>Whole Building (3D Stack)</span>
      </button>
    </div>

    <div class="floor-info-badge">
      <span class="climatic-pill">☀️ South Road • 🌬️ Stack Cooling</span>
      <span class="plot-pill">30' × 60' (1800 sq ft)</span>
    </div>
  </div>

  <!-- Main Workspace -->
  <div id="workspace">

    <!-- Floating Toggle Button for Furniture & Architectural Tools Drawer -->
    <button id="btn-toggle-catalog" title="Open Furniture Catalog & Tools">
      <span>🛋️</span>
      <span>Furniture & Tools</span>
    </button>

    <!-- Left Collapsible Drawer: Architectural Tools & Furniture Catalog -->
    <aside id="left-sidebar" class="collapsed">
      <div class="sidebar-header">
        <div class="sidebar-title-row">
          <span class="sidebar-title">🛋️ Furniture & Tools</span>
          <button id="btn-close-catalog" class="drawer-close-btn" title="Close Drawer">✕</button>
        </div>
        <div class="search-input-wrap">
          <span class="search-icon">🔍</span>
          <input type="text" id="catalog-search" class="search-input" placeholder="Search furniture...">
        </div>
      </div>

      <!-- Architectural Drawing Tools -->
      <div class="arch-tools-section">
        <button class="tool-btn active" data-tool="select" title="Select & Move Objects">
          <span class="tool-icon">👆</span>
          <span>Select</span>
        </button>
        <button class="tool-btn" data-tool="wall" title="Draw Wall">
          <span class="tool-icon">🧱</span>
          <span>Wall</span>
        </button>
        <button class="tool-btn" data-tool="door" title="Place Door">
          <span class="tool-icon">🚪</span>
          <span>Door</span>
        </button>
        <button class="tool-btn" data-tool="window" title="Place Window">
          <span class="tool-icon">🪟</span>
          <span>Window</span>
        </button>
      </div>

      <!-- Category Filter Tabs -->
      <nav class="catalog-nav">
        <button class="cat-tab active" data-cat="all">All</button>
        <button class="cat-tab" data-cat="living">🛋️ Living</button>
        <button class="cat-tab" data-cat="bedroom">🛏️ Bed</button>
        <button class="cat-tab" data-cat="kitchen">🍳 Kitchen</button>
        <button class="cat-tab" data-cat="bathroom">🚿 Bath</button>
        <button class="cat-tab" data-cat="decor">🌿 Decor</button>
      </nav>

      <!-- Catalog Cards Container -->
      <div id="catalog-content" class="catalog-content">
        <!-- Dynamically rendered by app.js -->
      </div>
    </aside>

    <!-- Center Viewport / Canvas Container (100% Expansive Canvas) -->
    <main id="viewport-container">
      <!-- 2D Blueprint Canvas -->
      <canvas id="floorplan-canvas" style="display: none;"></canvas>

      <!-- 3D Three.js Canvas Container -->
      <div id="threejs-canvas-container" style="display: block;"></div>

      <!-- Live Drawing Hint Tooltip -->
      <div id="drawing-hint">Click anywhere to start drawing wall.</div>

      <!-- Floating Camera Angle Presets (Bottom Center) -->
      <div id="camera-quick-bar" class="camera-quick-bar">
        <button class="cam-btn" data-preset="front">🏠 Front (South)</button>
        <button class="cam-btn" data-preset="top">🦅 Top View</button>
        <button class="cam-btn" data-preset="side">Side Elevation</button>
        <button class="cam-btn" data-preset="isometric">🔄 Reset 3D</button>
      </div>

      <!-- Floating Interaction Hint -->
      <div class="interaction-hint-pill">
        🖱️ Left-Click to Rotate • Scroll to Zoom • Right-Click to Pan
      </div>

      <!-- First-Person Walkthrough HUD -->
      <div id="walkthrough-hud">
        <div class="crosshair"></div>
        <div class="walkthrough-instructions">
          <span><span class="key-badge">W</span> <span class="key-badge">A</span> <span class="key-badge">S</span> <span class="key-badge">D</span> to Walk</span>
          <span>•</span>
          <span>Mouse to Look Around</span>
          <span>•</span>
          <span>Press <span class="key-badge">ESC</span> to Exit</span>
        </div>
      </div>
    </main>

    <!-- Floating Right Inspector Card (Opens on Selection) -->
    <aside id="right-sidebar" class="collapsed">
      <div class="inspector-header">
        <span class="inspector-title">Properties & Vastu</span>
        <button id="btn-close-inspector" class="inspector-close-btn" title="Close">✕</button>
      </div>
      <div id="inspector-content" class="inspector-body">
        <!-- Dynamically populated based on selection -->
      </div>
    </aside>
  </div>

  <!-- Bottom Status Bar -->
  <footer id="status-bar">
    <div class="status-left">
      <div class="status-item">
        <span>📍 Cursor:</span>
        <span class="status-val" id="status-coords">X: 0.00m, Y: 0.00m</span>
      </div>
      <div class="status-item">
        <span>📐 Area:</span>
        <span class="status-val" id="status-area">0 m²</span>
      </div>
    </div>
    <div class="status-right">
      <div class="status-item">
        <span>Shortcuts: <kbd>R</kbd> Rotate • <kbd>Del</kbd> Delete • <kbd>Esc</kbd> Deselect</span>
      </div>
    </div>
  </footer>

  <!-- Room Sizes & Vastu Guide Modal -->
  <div id="room-sizes-modal" class="modal-backdrop">
    <div class="modal-dialog" style="max-width: 680px;">
      <div class="modal-header">
        <h3 class="modal-title">📏 Complete Room Sizes & Vastu Guide</h3>
        <button id="modal-close-room-sizes" class="modal-close-btn">✕</button>
      </div>
      <div class="modal-body">
        <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 12px;">
          Plot: <b style="color: #f8fafc;">30'-0" × 60'-0" (1800 sq ft / 200 Gaj)</b> • Facing: <b style="color: #f59e0b;">South (Road)</b> • Location: <b style="color: #38bdf8;">Jodhpur, Rajasthan</b>
        </div>

        <h4 style="color: #38bdf8; font-size: 13px; margin: 10px 0 6px;">🏠 1st Floor & 2nd Floor (Identical Luxury 3BHK for Brothers)</h4>
        <table class="room-size-table">
          <thead>
            <tr>
              <th>Space / Room</th>
              <th>Dimensions</th>
              <th>Carpet Area</th>
              <th>Vastu Zone & Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>🚪 Private Entrance Foyer</b></td>
              <td>5'0" × 7'5"</td>
              <td>37 sq ft</td>
              <td><span class="vastu-tag sw">Entry Buffer Screen</span></td>
            </tr>
            <tr>
              <td><b>🛋️ Grand Open Living Hall</b></td>
              <td>13'6" to 22'6" × 25'0"</td>
              <td><b>~350 sq ft</b></td>
              <td><span class="vastu-tag cen">Dining Table Removed</span></td>
            </tr>
            <tr>
              <td><b>👑 Restored Master Suite</b></td>
              <td>11'3" × 19'8"</td>
              <td><b>221 sq ft</b></td>
              <td><span class="vastu-tag sw">Nairutya (SW)</span></td>
            </tr>
            <tr>
              <td><b>🛏️ Bedroom 3 (Study/Bed)</b></td>
              <td>15'0" × 14'6"</td>
              <td><b>217 sq ft</b></td>
              <td><span class="vastu-tag ne">Door to North Gali</span></td>
            </tr>
            <tr>
              <td><b>🌬️ Bedroom 2 (Children/Bed)</b></td>
              <td>15'0" × 14'6"</td>
              <td><b>217 sq ft</b></td>
              <td><span class="vastu-tag nw">Door to North Gali</span></td>
            </tr>
            <tr>
              <td><b>🔥 Modular Kitchen</b></td>
              <td>9'1" × 14'1"</td>
              <td>128 sq ft</td>
              <td><span class="vastu-tag se">Agneya (SE)</span></td>
            </tr>
            <tr>
              <td><b>🙏 Sacred Mandir (Pooja)</b></td>
              <td>5'8" × 5'6"</td>
              <td>31 sq ft</td>
              <td><span class="vastu-tag ne">Ishanya / East</span></td>
            </tr>
            <tr>
              <td><b>🌀 Central OTS Air Chimney</b></td>
              <td>5'0" × 5'0"</td>
              <td>25 sq ft</td>
              <td><span class="vastu-tag cen">Brahmasthan</span></td>
            </tr>
            <tr>
              <td><b>South Shaded Balcony</b></td>
              <td>30'0" × 4'5"</td>
              <td>132 sq ft</td>
              <td>South Front</td>
            </tr>
            <tr>
              <td><b>North Rear Common Gali</b></td>
              <td>30'0" × 4'0"</td>
              <td>120 sq ft</td>
              <td>Direct Door Access on All Floors</td>
            </tr>
          </tbody>
        </table>

        <h4 style="color: #38bdf8; font-size: 13px; margin: 18px 0 6px;">🅿️ Ground Floor (Common Stilt + 2 Rear Rooms)</h4>
        <table class="room-size-table">
          <thead>
            <tr>
              <th>Space / Room</th>
              <th>Dimensions</th>
              <th>Carpet Area</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>🅿️ Covered Stilt Parking</b></td>
              <td>30'0" × 41'6"</td>
              <td><b>~950 sq ft</b></td>
              <td>Fits 3–4 cars (SUVs) + 4–6 bikes</td>
            </tr>
            <tr>
              <td><b>🛏️ Rear Room 1 + Bath</b></td>
              <td>15'0" × 14'9"</td>
              <td>221 sq ft</td>
              <td>Door directly to North gali</td>
            </tr>
            <tr>
              <td><b>🛏️ Rear Room 2 + Bath</b></td>
              <td>15'0" × 14'9"</td>
              <td>221 sq ft</td>
              <td>Door directly to North gali</td>
            </tr>
            <tr>
              <td><b>🌬️ North Rear Gali</b></td>
              <td>30'0" × 3'9"</td>
              <td>112 sq ft</td>
              <td>Open-to-sky cool air reservoir</td>
            </tr>
            <tr>
              <td><b>SW Staircase & Lift Core</b></td>
              <td>7'6" × 14'7"</td>
              <td>110 sq ft</td>
              <td>Dedicated 5'×5' elevator shaft</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- Template Selection Modal (Hidden Fallback) -->
  <div id="templates-modal" class="modal-backdrop">
    <div class="modal-dialog">
      <div class="modal-header">
        <h3 class="modal-title">Select Template</h3>
        <button id="modal-close" class="modal-close-btn">✕</button>
      </div>
      <div class="modal-body">
        <div id="template-list" class="template-card-grid"></div>
      </div>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div id="toast-container"></div>

  <!-- CDN Three.js Core & Controls (Cloudflare CDNJS & jsDelivr) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.js"></script>

  <!-- Local fallback if CDN is offline -->
  <script>
    if (typeof THREE === 'undefined') {{
      document.write('<script src="js/lib/three.min.js"><\\/script>');
      document.write('<script src="js/lib/OrbitControls.js"><\\/script>');
      document.write('<script src="js/lib/PointerLockControls.js"><\\/script>');
    }}
  </script>

  <!-- Inlined Application Logic (Zero-dependency & Self-Contained) -->
  <script>
{combined_js}
  </script>
</body>
</html>
"""

# Write out index.html
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated clean, easy, and simple index.html! Size:", len(html_template), "bytes")
