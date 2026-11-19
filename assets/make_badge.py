#!/usr/bin/env python3
"""Generate a clean vector BusinessRate "RANKED #1 / AWARD WINNER" shield badge.

Recreated from the client's physical certificate (MG Woodshop & More —
Ranked #1 Carpenter in Cypress for 2026, June 2026 Award Winner).

Outputs:
  assets/businessrate-2026-badge.svg  (crisp at any size, for the web)
  assets/businessrate-2026-badge.png  (transparent 2x raster, for email/social)

Note: cairosvg mis-renders <text> with nested <tspan> under text-anchor=middle,
so the two-tone "BusinessRate" wordmark is laid out with two measured plain
<text> runs (Liberation Sans is metric-compatible with Arial/Helvetica, so the
browser renders the same widths).
"""
import math
from PIL import ImageFont

W, H = 560, 700
NAVY = "#17212E"
GOLD = "#C9A227"
GOLD_LIGHT = "#DFBE6A"
CREAM = "#F3F1EC"
INK = "#16202E"

BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def width(text, path, size):
    f = ImageFont.truetype(path, size)
    return f.getlength(text)


def star(cx, cy, r, color=GOLD_LIGHT):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.44
        pts.append(f"{cx + rad * math.cos(ang):.1f},{cy + rad * math.sin(ang):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{color}"/>'


outer = ("M 34,5 L 526,5 Q 555,5 555,34 L 555,548 "
         "L 280,694 L 5,548 L 5,34 Q 5,5 34,5 Z")
inner = ("M 46,20 L 514,20 Q 539,20 539,45 L 539,542 "
         "L 280,668 L 21,542 L 21,45 Q 21,20 46,20 Z")

# --- two-tone wordmark, centred in the band -------------------------------
SIZE = 47
w_bold = width("Business", BOLD, SIZE)
w_reg = width("Rate", REG, SIZE)
start = 280 - (w_bold + w_reg) / 2
x_rate = start + w_bold

FONT = "Liberation Sans, Helvetica Neue, Helvetica, Arial, sans-serif"

svgns = 'xmlns="http://www.w3.org/2000/svg"'
svg = f'''<svg {svgns} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="BusinessRate Ranked #1 Award Winner - June 2026">
  <title>BusinessRate RANKED #1 - Award Winner - June 2026</title>
  <defs>
    <linearGradient id="plate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1B2735"/>
      <stop offset="55%" stop-color="{NAVY}"/>
      <stop offset="100%" stop-color="#101822"/>
    </linearGradient>
    <linearGradient id="goldfill" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E9D191"/>
      <stop offset="50%" stop-color="{GOLD_LIGHT}"/>
      <stop offset="100%" stop-color="#B8892B"/>
    </linearGradient>
  </defs>

  <!-- shield plate -->
  <path d="{outer}" fill="url(#plate)" stroke="url(#goldfill)" stroke-width="9" stroke-linejoin="round"/>
  <path d="{inner}" fill="none" stroke="{GOLD_LIGHT}" stroke-width="2.5" stroke-opacity="0.65"/>

  <!-- RANKED #1 -->
  <text x="280" y="96" text-anchor="middle" font-family="{FONT}"
        font-size="58" font-weight="bold" letter-spacing="3" fill="url(#goldfill)">RANKED #1</text>

  <!-- BusinessRate band -->
  <rect x="30" y="124" width="500" height="112" rx="10" fill="{CREAM}" stroke="url(#goldfill)" stroke-width="5"/>
  <text x="{start:.1f}" y="196" font-family="{FONT}" font-size="{SIZE}" font-weight="bold" fill="{INK}">Business</text>
  <text x="{x_rate:.1f}" y="196" font-family="{FONT}" font-size="{SIZE}" font-weight="normal" fill="{INK}">Rate</text>

  <!-- JUNE / 2026 -->
  <text x="280" y="292" text-anchor="middle" font-family="{FONT}"
        font-size="38" font-weight="normal" letter-spacing="9" fill="{CREAM}">JUNE</text>
  <text x="280" y="404" text-anchor="middle" font-family="{FONT}"
        font-size="106" font-weight="bold" letter-spacing="1" fill="{CREAM}">2026</text>

  <!-- side accents -->
  <path d="M 62,268 L 62,470" stroke="{GOLD_LIGHT}" stroke-width="3.5" stroke-opacity="0.9"/>
  <path d="M 498,268 L 498,470" stroke="{GOLD_LIGHT}" stroke-width="3.5" stroke-opacity="0.9"/>

  <!-- AWARD WINNER -->
  <text x="280" y="466" text-anchor="middle" font-family="{FONT}"
        font-size="29" font-weight="bold" letter-spacing="4.5" fill="#EFE3BC">AWARD WINNER</text>

  <!-- stars -->
  {star(280, 560, 27)}
  {star(232, 560, 20)}
  {star(328, 560, 20)}
  {star(190, 560, 15)}
  {star(370, 560, 15)}
</svg>
'''

open("/root/mgwoodshop-repo/assets/businessrate-2026-badge.svg", "w").write(svg)
print("svg written", len(svg))
