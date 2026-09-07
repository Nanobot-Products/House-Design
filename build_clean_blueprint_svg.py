# build_clean_blueprint_svg.py
import os

base_dir = r"C:\Users\vikas\.gemini\antigravity\scratch\house-interior-3d-designer"
artifact_dir = r"C:\Users\vikas\.gemini\antigravity\brain\07fc00bd-14a6-40ec-b134-9813e03c1f1c"

def generate_first_floor_svg():
    # Scale: 1 ft = 20 px
    # Plot: 30 ft (600 px) x 60 ft (1200 px)
    # Origin: x=120, y=100
    ox, oy = 120, 100
    pw, ph = 600, 1200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 1480" width="840" height="1480" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="hatch" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#cbd5e1" stroke-width="1.5" />
    </pattern>
    <marker id="tick" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <line x1="0" y1="10" x2="10" y2="0" stroke="#000000" stroke-width="2"/>
    </marker>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- Title & Orientation Banner -->
  <text x="420" y="38" text-anchor="middle" font-size="22" font-weight="800" fill="#0f172a" letter-spacing="1">1ST &amp; 2ND FLOOR PLAN (3BHK)</text>
  <text x="420" y="62" text-anchor="middle" font-size="13" font-weight="600" fill="#64748b">30' × 60' • SOUTH FACING • 100% HINDU VASTU SHASTRA</text>

  <!-- EXTERIOR DIMENSION LINES (Like Reference Image) -->
  <!-- Top Dimension: 30' -->
  <line x1="{ox}" y1="80" x2="{ox+pw}" y2="80" stroke="#000000" stroke-width="1.5" marker-start="url(#tick)" marker-end="url(#tick)" />
  <line x1="{ox}" y1="70" x2="{ox}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="{ox+pw}" y1="70" x2="{ox+pw}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="385" y="68" width="70" height="24" fill="#ffffff"/>
  <text x="420" y="86" text-anchor="middle" font-size="18" font-weight="800" fill="#000000">30'</text>

  <!-- Left Dimension: 60' -->
  <line x1="70" y1="{oy}" x2="70" y2="{oy+ph}" stroke="#000000" stroke-width="1.5" marker-start="url(#tick)" marker-end="url(#tick)" />
  <line x1="60" y1="{oy}" x2="{ox}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="60" y1="{oy+ph}" x2="{ox}" y2="{oy+ph}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="50" y="{oy + ph/2}" text-anchor="middle" font-size="18" font-weight="800" fill="#000000" transform="rotate(-90 50 {oy + ph/2})">60'</text>

  <!-- Right Dimension: 60' -->
  <line x1="770" y1="{oy}" x2="770" y2="{oy+ph}" stroke="#000000" stroke-width="1.5" marker-start="url(#tick)" marker-end="url(#tick)" />
  <line x1="760" y1="{oy}" x2="{ox+pw}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="760" y1="{oy+ph}" x2="{ox+pw}" y2="{oy+ph}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="790" y="{oy + ph/2}" text-anchor="middle" font-size="18" font-weight="800" fill="#000000" transform="rotate(90 790 {oy + ph/2})">60'</text>

  <!-- BUILDING PLOT BOUNDARY -->
  <rect x="{ox}" y="{oy}" width="{pw}" height="{ph}" fill="#f8fafc" stroke="#000000" stroke-width="3.5" />

  <!-- 1. NORTH REAR GALI (30'0" x 4'0" = 600px x 80px) -->
  <rect x="{ox}" y="{oy}" width="{pw}" height="80" fill="#e2e8f0" stroke="#000000" stroke-width="2" />
  <text x="420" y="{oy+45}" text-anchor="middle" font-size="14" font-weight="800" fill="#0f172a">COMMON REAR GALI (COOL AIR RESERVOIR)</text>
  <text x="420" y="{oy+65}" text-anchor="middle" font-size="12" font-weight="700" fill="#0284c7">30'0" × 4'0"</text>

  <!-- 2. REAR BEDROOMS (Depth: 14'6" = 290px, y = oy+80=180 to 470) -->
  <!-- Dividing Wall between Bed 2 and Bed 3 at x = ox+300 = 420 -->
  <line x1="420" y1="180" x2="420" y2="470" stroke="#000000" stroke-width="3" />
  <line x1="{ox}" y1="470" x2="{ox+pw}" y2="470" stroke="#000000" stroke-width="3" />

  <!-- BEDROOM 2 (NW / Vayavya, 15'0" x 14'6") -->
  <rect x="{ox}" y="180" width="300" height="290" fill="#ffffff" stroke="none" />
  <!-- Attached Washroom 2 (6'0" x 6'0" = 120 x 120) -->
  <rect x="{ox}" y="180" width="120" height="120" fill="#f1f5f9" stroke="#000000" stroke-width="2" />
  <text x="{ox+60}" y="235" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">A.WASH</text>
  <text x="{ox+60}" y="252" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">ROOM</text>
  <text x="{ox+60}" y="272" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">6'0" × 6'0"</text>
  <!-- Washroom WC icon -->
  <rect x="{ox+20}" y="195" width="22" height="30" rx="10" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <!-- Bedroom 2 Bed & Labels -->
  <rect x="230" y="270" width="130" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <rect x="230" y="390" width="130" height="30" fill="#e2e8f0" stroke="#000000" stroke-width="1" />
  <text x="295" y="335" text-anchor="middle" font-size="14" font-weight="800" fill="#000000">BEDROOM 2</text>
  <text x="295" y="358" text-anchor="middle" font-size="13" font-weight="700" fill="#0284c7">15'0" × 14'6"</text>
  <!-- Bedroom 2 Dimensions lines -->
  <line x1="{ox+130}" y1="200" x2="410" y2="200" stroke="#000000" stroke-width="1" marker-start="url(#tick)" marker-end="url(#tick)" />
  <text x="295" y="195" text-anchor="middle" font-size="11" font-weight="700">15'0"</text>
  <line x1="410" y1="210" x2="410" y2="460" stroke="#000000" stroke-width="1" marker-start="url(#tick)" marker-end="url(#tick)" />
  <text x="395" y="335" text-anchor="middle" font-size="11" font-weight="700" transform="rotate(-90 395 335)">14'6"</text>
  <!-- Door to Rear Gali -->
  <line x1="160" y1="180" x2="160" y2="155" stroke="#0284c7" stroke-width="2"/>
  <path d="M 160 155 A 25 25 0 0 1 185 180" fill="none" stroke="#0284c7" stroke-dasharray="2,2"/>
  <text x="175" y="172" font-size="9" font-weight="bold" fill="#0284c7">DOOR</text>

  <!-- BEDROOM 3 (NE / Ishanya side, 15'0" x 14'6") -->
  <rect x="420" y="180" width="300" height="290" fill="#ffffff" stroke="none" />
  <!-- Attached Washroom 3 (6'0" x 6'0" = 120 x 120 on East) -->
  <rect x="600" y="180" width="120" height="120" fill="#f1f5f9" stroke="#000000" stroke-width="2" />
  <text x="660" y="235" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">A.WASH</text>
  <text x="660" y="252" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">ROOM</text>
  <text x="660" y="272" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">6'0" × 6'0"</text>
  <!-- Washroom WC icon -->
  <rect x="680" y="195" width="22" height="30" rx="10" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <!-- Bedroom 3 Bed & Labels -->
  <rect x="450" y="270" width="130" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <rect x="450" y="390" width="130" height="30" fill="#e2e8f0" stroke="#000000" stroke-width="1" />
  <text x="515" y="335" text-anchor="middle" font-size="14" font-weight="800" fill="#000000">BEDROOM 3</text>
  <text x="515" y="358" text-anchor="middle" font-size="13" font-weight="700" fill="#0284c7">15'0" × 14'6"</text>
  <!-- Bedroom 3 Dimensions lines -->
  <line x1="430" y1="200" x2="590" y2="200" stroke="#000000" stroke-width="1" marker-start="url(#tick)" marker-end="url(#tick)" />
  <text x="510" y="195" text-anchor="middle" font-size="11" font-weight="700">15'0"</text>
  <line x1="430" y1="210" x2="430" y2="460" stroke="#000000" stroke-width="1" marker-start="url(#tick)" marker-end="url(#tick)" />
  <text x="445" y="335" text-anchor="middle" font-size="11" font-weight="700" transform="rotate(-90 445 335)">14'6"</text>
  <!-- Door to Rear Gali -->
  <line x1="550" y1="180" x2="550" y2="155" stroke="#0284c7" stroke-width="2"/>
  <path d="M 550 155 A 25 25 0 0 1 575 180" fill="none" stroke="#0284c7" stroke-dasharray="2,2"/>
  <text x="560" y="172" font-size="9" font-weight="bold" fill="#0284c7">DOOR</text>

  <!-- 3. MIDDLE ZONE (y = 470 to 863) -->
  <!-- MASTER BEDROOM (Nairutya / SW, 11'3" x 19'8" = 225px x 393px) -->
  <rect x="{ox}" y="470" width="225" height="393" fill="#ffffff" stroke="#000000" stroke-width="3" />
  <!-- Master Bath (6'0" x 6'6" = 120 x 130) -->
  <rect x="{ox}" y="470" width="120" height="130" fill="#f1f5f9" stroke="#000000" stroke-width="2" />
  <text x="{ox+60}" y="525" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">A.WASH</text>
  <text x="{ox+60}" y="542" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">ROOM</text>
  <text x="{ox+60}" y="562" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">6'0" × 6'6"</text>
  <!-- Master Bed & Labels -->
  <rect x="{ox+50}" y="660" width="140" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <rect x="{ox+50}" y="660" width="140" height="30" fill="#e2e8f0" stroke="#000000" stroke-width="1" />
  <text x="{ox+120}" y="735" text-anchor="middle" font-size="13" font-weight="800" fill="#000000">MASTER</text>
  <text x="{ox+120}" y="753" text-anchor="middle" font-size="13" font-weight="800" fill="#000000">BEDROOM</text>
  <text x="{ox+120}" y="775" text-anchor="middle" font-size="12" font-weight="700" fill="#0284c7">11'3" × 19'8"</text>
  <!-- Master Dimensions -->
  <line x1="{ox+130}" y1="485" x2="335" y2="485" stroke="#000000" stroke-width="1" marker-start="url(#tick)" marker-end="url(#tick)" />
  <text x="235" y="480" text-anchor="middle" font-size="10" font-weight="700">11'3"</text>
  <line x1="335" y1="485" x2="335" y2="850" stroke="#000000" stroke-width="1" marker-start="url(#tick)" marker-end="url(#tick)" />
  <text x="320" y="660" text-anchor="middle" font-size="11" font-weight="700" transform="rotate(-90 320 660)">19'8"</text>

  <!-- CENTRAL OTS (5'0" x 5'0" = 100 x 100) -->
  <rect x="365" y="550" width="100" height="100" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" />
  <line x1="365" y1="550" x2="465" y2="650" stroke="#38bdf8" stroke-width="1.5" />
  <line x1="465" y1="550" x2="365" y2="650" stroke="#38bdf8" stroke-width="1.5" />
  <text x="415" y="595" text-anchor="middle" font-size="12" font-weight="800" fill="#0369a1">OTS</text>
  <text x="415" y="612" text-anchor="middle" font-size="10" font-weight="700" fill="#0369a1">5'0" × 5'0"</text>

  <!-- COMMON WASHROOM (5'0" x 4'3" = 100 x 85) -->
  <rect x="365" y="470" width="100" height="75" fill="#f1f5f9" stroke="#000000" stroke-width="2" />
  <text x="415" y="505" text-anchor="middle" font-size="10" font-weight="800" fill="#0f172a">C.TOILET</text>
  <text x="415" y="520" text-anchor="middle" font-size="9" font-weight="600" fill="#475569">5'0" × 4'3"</text>

  <!-- SACRED POOJA MANDIR (5'8" x 5'6" = 113 x 110 on East) -->
  <rect x="607" y="580" width="113" height="110" fill="#fef9c3" stroke="#eab308" stroke-width="2" />
  <text x="663" y="630" text-anchor="middle" font-size="12" font-weight="800" fill="#854d0e">POOJA</text>
  <text x="663" y="648" text-anchor="middle" font-size="10" font-weight="700" fill="#854d0e">MANDIR</text>
  <text x="663" y="666" text-anchor="middle" font-size="10" font-weight="600" fill="#a16207">5'8" × 5'6"</text>

  <!-- 4. FRONT ZONE (y = 863 to 1210) -->
  <!-- STAIRCASE & LIFT CORE (SW, 7'6" x 14'7" = 150px x 292px) -->
  <rect x="{ox}" y="863" width="150" height="292" fill="#f8fafc" stroke="#000000" stroke-width="3" />
  <!-- Dedicated Lift Shaft (5'0" x 5'0" = 100 x 100) -->
  <rect x="{ox}" y="863" width="100" height="100" fill="#e2e8f0" stroke="#000000" stroke-width="2" />
  <text x="{ox+50}" y="912" text-anchor="middle" font-size="12" font-weight="800" fill="#0f172a">LIFT</text>
  <text x="{ox+50}" y="930" text-anchor="middle" font-size="10" font-weight="700" fill="#475569">5'0" × 5'0"</text>
  <!-- Stair treads -->
  {chr(10).join([f'<line x1="{ox}" y1="{980 + i*17}" x2="{ox+150}" y2="{980 + i*17}" stroke="#94a3b8" stroke-width="1.2" />' for i in range(10)])}
  <text x="{ox+75}" y="1070" text-anchor="middle" font-size="13" font-weight="800" fill="#000000">STAIRS 7'6"</text>

  <!-- ENTRANCE FOYER WITH PRIVACY SCREEN (5'0" x 7'5" = 100 x 150) -->
  <rect x="270" y="863" width="90" height="145" fill="#f8fafc" stroke="none" />
  <!-- Privacy Buffer Screen -->
  <line x1="360" y1="863" x2="360" y2="990" stroke="#0284c7" stroke-width="4" stroke-linecap="round"/>
  <text x="315" y="930" text-anchor="middle" font-size="11" font-weight="800" fill="#0284c7">ENTRANCE</text>
  <text x="315" y="948" text-anchor="middle" font-size="11" font-weight="800" fill="#0284c7">FOYER</text>
  <text x="315" y="966" text-anchor="middle" font-size="9" font-weight="600" fill="#0369a1">5'0" × 7'5"</text>
  <!-- Apartment Main Door -->
  <line x1="270" y1="895" x2="295" y2="895" stroke="#000000" stroke-width="2"/>
  <path d="M 295 895 A 25 25 0 0 1 270 920" fill="none" stroke="#000000" stroke-dasharray="2,2"/>

  <!-- MODULAR KITCHEN (SE / Agneya, 9'1" x 14'1" = 182 x 282) -->
  <rect x="538" y="873" width="182" height="282" fill="#ffffff" stroke="#000000" stroke-width="3" />
  <!-- L-shaped kitchen counter -->
  <rect x="538" y="873" width="182" height="40" fill="#f1f5f9" stroke="#000000" stroke-width="1.5" />
  <rect x="680" y="873" width="40" height="282" fill="#f1f5f9" stroke="#000000" stroke-width="1.5" />
  <text x="615" y="1000" text-anchor="middle" font-size="14" font-weight="800" fill="#000000">KITCHEN</text>
  <text x="615" y="1022" text-anchor="middle" font-size="13" font-weight="700" fill="#d97706">9'1" × 14'1"</text>
  <text x="615" y="1040" text-anchor="middle" font-size="10" font-weight="600" fill="#b45309">(AGNEYA / SE)</text>
  <!-- Stove Icon facing East -->
  <circle cx="698" cy="990" r="10" fill="#ea580c"/>
  <circle cx="698" cy="1020" r="10" fill="#ea580c"/>
  <text x="698" y="1055" text-anchor="middle" font-size="9" font-weight="bold" fill="#ea580c">EAST STOVE</text>

  <!-- GRAND OPEN LIVING & ENTERTAINING HALL (~350 sq ft) -->
  <!-- Sofa arrangement in front hall -->
  <rect x="380" y="1030" width="135" height="90" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <rect x="420" y="1050" width="55" height="50" fill="#f1f5f9" stroke="#000000" stroke-width="1" />
  <text x="450" y="970" text-anchor="middle" font-size="15" font-weight="800" fill="#000000">GRAND LIVING HALL</text>
  <text x="450" y="995" text-anchor="middle" font-size="14" font-weight="800" fill="#0284c7">13'6" to 22'6" × 25'0"</text>
  <text x="450" y="1015" text-anchor="middle" font-size="11" font-weight="600" fill="#64748b">(~350 SQ FT OPEN GREAT ROOM)</text>

  <!-- 5. SOUTH SHADED BALCONY (30'0" x 4'5" = 600 x 90) -->
  <rect x="{ox}" y="1155" width="{pw}" height="90" fill="#f1f5f9" stroke="#000000" stroke-width="2.5" />
  <text x="420" y="1200" text-anchor="middle" font-size="14" font-weight="800" fill="#0f172a">SOUTH SHADED BALCONY (CHHAJJA)</text>
  <text x="420" y="1220" text-anchor="middle" font-size="12" font-weight="700" fill="#0284c7">30'0" × 4'5"</text>

  <!-- FRONT ROAD BANNER -->
  <rect x="{ox}" y="1255" width="{pw}" height="45" fill="#0f172a" />
  <text x="420" y="1283" text-anchor="middle" font-size="14" font-weight="800" fill="#f8fafc" letter-spacing="1">▼ 30 FT WIDE FRONT ROAD (SOUTH FACING) ▼</text>
</svg>
'''
    return svg

def generate_ground_floor_svg():
    ox, oy = 120, 100
    pw, ph = 600, 1200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 1480" width="840" height="1480" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <marker id="tick2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <line x1="0" y1="10" x2="10" y2="0" stroke="#000000" stroke-width="2"/>
    </marker>
  </defs>

  <!-- Title & Orientation Banner -->
  <text x="420" y="38" text-anchor="middle" font-size="22" font-weight="800" fill="#0f172a" letter-spacing="1">GROUND FLOOR PLAN (COMMON)</text>
  <text x="420" y="62" text-anchor="middle" font-size="13" font-weight="600" fill="#64748b">30' × 60' • STILT PARKING + 2 REAR ROOMS + ATTACHED GALI</text>

  <!-- EXTERIOR DIMENSION LINES -->
  <line x1="{ox}" y1="80" x2="{ox+pw}" y2="80" stroke="#000000" stroke-width="1.5" marker-start="url(#tick2)" marker-end="url(#tick2)" />
  <line x1="{ox}" y1="70" x2="{ox}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="{ox+pw}" y1="70" x2="{ox+pw}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="385" y="68" width="70" height="24" fill="#ffffff"/>
  <text x="420" y="86" text-anchor="middle" font-size="18" font-weight="800" fill="#000000">30'</text>

  <line x1="70" y1="{oy}" x2="70" y2="{oy+ph}" stroke="#000000" stroke-width="1.5" marker-start="url(#tick2)" marker-end="url(#tick2)" />
  <line x1="60" y1="{oy}" x2="{ox}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="60" y1="{oy+ph}" x2="{ox}" y2="{oy+ph}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="50" y="{oy + ph/2}" text-anchor="middle" font-size="18" font-weight="800" fill="#000000" transform="rotate(-90 50 {oy + ph/2})">60'</text>

  <line x1="770" y1="{oy}" x2="770" y2="{oy+ph}" stroke="#000000" stroke-width="1.5" marker-start="url(#tick2)" marker-end="url(#tick2)" />
  <line x1="760" y1="{oy}" x2="{ox+pw}" y2="{oy}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="760" y1="{oy+ph}" x2="{ox+pw}" y2="{oy+ph}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="790" y="{oy + ph/2}" text-anchor="middle" font-size="18" font-weight="800" fill="#000000" transform="rotate(90 790 {oy + ph/2})">60'</text>

  <!-- PLOT BOUNDARY -->
  <rect x="{ox}" y="{oy}" width="{pw}" height="{ph}" fill="#f8fafc" stroke="#000000" stroke-width="3.5" />

  <!-- 1. NORTH REAR GALI (30'0" x 3'9" = 600 x 75) -->
  <rect x="{ox}" y="{oy}" width="{pw}" height="75" fill="#e2e8f0" stroke="#000000" stroke-width="2" />
  <text x="420" y="{oy+42}" text-anchor="middle" font-size="13" font-weight="800" fill="#0f172a">NORTH REAR GALI (VENTILATION CORRIDOR)</text>
  <text x="420" y="{oy+60}" text-anchor="middle" font-size="11" font-weight="700" fill="#0284c7">30'0" × 3'9"</text>

  <!-- 2. REAR ROOMS (y = 175 to 470, depth = 14'9" = 295px) -->
  <line x1="420" y1="175" x2="420" y2="470" stroke="#000000" stroke-width="3" />
  <line x1="{ox}" y1="470" x2="{ox+pw}" y2="470" stroke="#000000" stroke-width="3.5" />

  <!-- REAR ROOM 1 (NW, 15'0" x 14'9") -->
  <rect x="{ox}" y="175" width="300" height="295" fill="#ffffff" stroke="none" />
  <rect x="{ox}" y="175" width="130" height="120" fill="#f1f5f9" stroke="#000000" stroke-width="2" />
  <text x="{ox+65}" y="235" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">A.WASH</text>
  <text x="{ox+65}" y="252" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">ROOM</text>
  <text x="{ox+65}" y="272" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">6'6" × 6'0"</text>
  <!-- Bed & Labels -->
  <rect x="230" y="270" width="130" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="295" y="335" text-anchor="middle" font-size="14" font-weight="800" fill="#000000">REAR ROOM 1</text>
  <text x="295" y="358" text-anchor="middle" font-size="13" font-weight="700" fill="#0284c7">15'0" × 14'9"</text>
  <text x="295" y="378" text-anchor="middle" font-size="10" font-weight="600" fill="#64748b">(GUEST / OFFICE)</text>
  <!-- Door to Gali -->
  <line x1="170" y1="175" x2="170" y2="150" stroke="#0284c7" stroke-width="2"/>
  <path d="M 170 150 A 25 25 0 0 1 195 175" fill="none" stroke="#0284c7" stroke-dasharray="2,2"/>
  <text x="185" y="167" font-size="9" font-weight="bold" fill="#0284c7">DOOR</text>

  <!-- REAR ROOM 2 (NE, 15'0" x 14'9") -->
  <rect x="420" y="175" width="300" height="295" fill="#ffffff" stroke="none" />
  <rect x="575" y="175" width="145" height="120" fill="#f1f5f9" stroke="#000000" stroke-width="2" />
  <text x="647" y="235" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">A.WASH</text>
  <text x="647" y="252" text-anchor="middle" font-size="11" font-weight="800" fill="#0f172a">ROOM</text>
  <text x="647" y="272" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">7'3" × 6'0"</text>
  <!-- Bed & Labels -->
  <rect x="450" y="270" width="130" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="515" y="335" text-anchor="middle" font-size="14" font-weight="800" fill="#000000">REAR ROOM 2</text>
  <text x="515" y="358" text-anchor="middle" font-size="13" font-weight="700" fill="#0284c7">15'0" × 14'9"</text>
  <text x="515" y="378" text-anchor="middle" font-size="10" font-weight="600" fill="#64748b">(ELDER / STAY)</text>
  <!-- Door to Gali -->
  <line x1="535" y1="175" x2="535" y2="150" stroke="#0284c7" stroke-width="2"/>
  <path d="M 535 150 A 25 25 0 0 1 560 175" fill="none" stroke="#0284c7" stroke-dasharray="2,2"/>
  <text x="548" y="167" font-size="9" font-weight="bold" fill="#0284c7">DOOR</text>

  <!-- 3. FRONT & MIDDLE ZONE (STILT PARKING + SW STAIRS/LIFT) -->
  <!-- STAIRCASE & LIFT CORE (SW, 7'6" x 14'7" = 150 x 292, y = 950 to 1242) -->
  <rect x="{ox}" y="950" width="150" height="292" fill="#f8fafc" stroke="#000000" stroke-width="3" />
  <rect x="{ox}" y="950" width="100" height="100" fill="#e2e8f0" stroke="#000000" stroke-width="2" />
  <text x="{ox+50}" y="1000" text-anchor="middle" font-size="12" font-weight="800" fill="#0f172a">LIFT</text>
  <text x="{ox+50}" y="1018" text-anchor="middle" font-size="10" font-weight="700" fill="#475569">5'0" × 5'0"</text>
  {chr(10).join([f'<line x1="{ox}" y1="{1065 + i*17}" x2="{ox+150}" y2="{1065 + i*17}" stroke="#94a3b8" stroke-width="1.2" />' for i in range(10)])}
  <text x="{ox+75}" y="1150" text-anchor="middle" font-size="13" font-weight="800" fill="#000000">STAIRS 7'6"</text>

  <!-- COVERED PARKING AREA (22'6" x 41'6" net) -->
  <!-- Car Silhouettes like Reference Image -->
  <!-- Car 1 -->
  <g transform="translate(320, 720)">
    <rect x="0" y="0" width="95" height="190" rx="20" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <rect x="12" y="35" width="71" height="50" rx="8" fill="#1e293b"/>
    <rect x="15" y="115" width="65" height="40" rx="6" fill="#334155"/>
    <rect x="5" y="172" width="15" height="8" rx="3" fill="#ef4444"/>
    <rect x="75" y="172" width="15" height="8" rx="3" fill="#ef4444"/>
  </g>
  <!-- Car 2 -->
  <g transform="translate(480, 720)">
    <rect x="0" y="0" width="95" height="190" rx="20" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <rect x="12" y="35" width="71" height="50" rx="8" fill="#1e293b"/>
    <rect x="15" y="115" width="65" height="40" rx="6" fill="#334155"/>
    <rect x="5" y="172" width="15" height="8" rx="3" fill="#ef4444"/>
    <rect x="75" y="172" width="15" height="8" rx="3" fill="#ef4444"/>
  </g>

  <text x="450" y="580" text-anchor="middle" font-size="18" font-weight="800" fill="#000000">COVERED STILT PARKING</text>
  <text x="450" y="610" text-anchor="middle" font-size="16" font-weight="800" fill="#0284c7">22'6" × 41'6"</text>
  <text x="450" y="635" text-anchor="middle" font-size="12" font-weight="600" fill="#64748b">(Accommodates 3–4 SUVs/Cars + 4–6 Bikes)</text>

  <!-- Dimension across parking width -->
  <line x1="280" y1="960" x2="710" y2="960" stroke="#000000" stroke-width="1" marker-start="url(#tick2)" marker-end="url(#tick2)" />
  <text x="495" y="953" text-anchor="middle" font-size="12" font-weight="800">22'6"</text>

  <!-- MAIN GATE AT BOTTOM -->
  <rect x="300" y="1242" width="380" height="15" fill="#0284c7" stroke="#000000" stroke-width="2"/>
  <text x="490" y="1235" text-anchor="middle" font-size="12" font-weight="800" fill="#0284c7">MAIN ENTRANCE GATE (19'0")</text>

  <!-- FRONT ROAD BANNER -->
  <rect x="{ox}" y="1255" width="{pw}" height="45" fill="#0f172a" />
  <text x="420" y="1283" text-anchor="middle" font-size="14" font-weight="800" fill="#f8fafc" letter-spacing="1">▼ 30 FT WIDE FRONT ROAD (SOUTH FACING) ▼</text>
</svg>
'''
    return svg

# Write SVGs to workspace and brain artifacts
f1_svg = generate_first_floor_svg()
gf_svg = generate_ground_floor_svg()

with open(os.path.join(base_dir, "floor1_blueprint.svg"), "w", encoding="utf-8") as f:
    f.write(f1_svg)

with open(os.path.join(base_dir, "ground_blueprint.svg"), "w", encoding="utf-8") as f:
    f.write(gf_svg)

with open(os.path.join(artifact_dir, "floor1_blueprint.svg"), "w", encoding="utf-8") as f:
    f.write(f1_svg)

with open(os.path.join(artifact_dir, "ground_blueprint.svg"), "w", encoding="utf-8") as f:
    f.write(gf_svg)

print("Generated clean architectural blueprint SVGs successfully!")
