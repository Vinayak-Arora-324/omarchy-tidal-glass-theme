#!/usr/bin/env python3
"""Generate the Tidal Glass wallpapers as SVG (render with rsvg-convert)."""
import math, os, sys

W, H = 3840, 2400
out = sys.argv[1] if len(sys.argv) > 1 else "build"
os.makedirs(out, exist_ok=True)

def wave(y0, amp, comps, phase, steps=160, bottom=True):
    pts = []
    for i in range(steps + 1):
        x = W * i / steps
        t = x / W
        y = y0 + sum(a * math.sin(2 * math.pi * (f * t) + p + phase) for a, f, p in comps) * amp
        pts.append((x, y))
    d = f"M -10 {H + 10} L -10 {pts[0][1]:.1f} "
    d += " ".join(f"L {x:.1f} {y:.1f}" for x, y in pts)
    d += f" L {W + 10} {H + 10} Z"
    return d

def wave_line(y0, amp, comps, phase, steps=200):
    pts = []
    for i in range(steps + 1):
        x = W * i / steps
        t = x / W
        y = y0 + sum(a * math.sin(2 * math.pi * (f * t) + p + phase) for a, f, p in comps) * amp
        pts.append((x, y))
    return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)

GRAIN = """
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="n"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.06"/></feComponentTransfer>
  </filter>"""

def svg(defs, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{GRAIN}
{defs}
</defs>
{body}
<rect width="{W}" height="{H}" filter="url(#grain)"/>
</svg>"""

# 1 — Tide: layered flowing hills of water, deep navy to luminous aqua.
layers = [
    (1150, 210, "#16324a", "#0f2236", 0.0),
    (1370, 190, "#1b4a63", "#123049", 1.3),
    (1580, 170, "#1f6a80", "#164158", 2.4),
    (1790, 150, "#2f93a8", "#1b5670", 3.7),
    (1990, 120, "#5cc2d4", "#25708a", 5.1),
    (2180, 90,  "#86d3df", "#2f7f99", 0.7),
]
defs = """<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#060b12"/><stop offset="0.55" stop-color="#0c1726"/><stop offset="1" stop-color="#13283d"/>
</linearGradient>
<radialGradient id="moon" cx="0.72" cy="0.28" r="0.45">
  <stop offset="0" stop-color="#9aaefa" stop-opacity="0.35"/><stop offset="1" stop-color="#9aaefa" stop-opacity="0"/>
</radialGradient>
<filter id="soft"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="shadow" x="-5%" y="-20%" width="110%" height="140%"><feGaussianBlur stdDeviation="40"/></filter>"""
body = f'<rect width="{W}" height="{H}" fill="url(#sky)"/><rect width="{W}" height="{H}" fill="url(#moon)"/>'
for i, (y, a, c1, c2, ph) in enumerate(layers):
    defs += f'<linearGradient id="l{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
    comps = [(1.0, 0.9, 0.3), (0.45, 1.7, 1.1), (0.2, 3.1, 2.2)]
    d = wave(y, a, comps, ph)
    body += f'<path d="{d}" fill="#02060b" opacity="0.55" transform="translate(0,-30)" filter="url(#shadow)"/>'
    body += f'<path d="{d}" fill="url(#l{i})"/>'
    body += f'<path d="{wave_line(y, a, comps, ph)}" fill="none" stroke="#e8fbff" stroke-opacity="{0.10 + i*0.04:.2f}" stroke-width="3" filter="url(#soft)"/>'
open(f"{out}/1-tide.svg", "w").write(svg(defs, body))

# 2 — Glass: soft luminous orbs drifting behind frosted glass.
defs = """<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#08101a"/><stop offset="1" stop-color="#0f1d2c"/>
</linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="220"/></filter>
<linearGradient id="pane" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#ffffff" stop-opacity="0.06"/><stop offset="1" stop-color="#ffffff" stop-opacity="0.015"/>
</linearGradient>"""
orbs = [(1050, 900, 720, "#2b9fc4", 0.85), (2750, 700, 640, "#7f8ff0", 0.70),
        (2300, 1750, 820, "#1fb5a8", 0.55), (700, 1950, 520, "#b7a2f0", 0.35),
        (3400, 1900, 460, "#6cc7e8", 0.45)]
body = f'<rect width="{W}" height="{H}" fill="url(#bg)"/><g filter="url(#blur)">'
body += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}"/>' for x, y, r, c, o in orbs)
body += "</g>"
body += f'<rect x="760" y="520" width="2320" height="1360" rx="96" fill="url(#pane)" stroke="#ffffff" stroke-opacity="0.10" stroke-width="3"/>'
open(f"{out}/2-glass.svg", "w").write(svg(defs, body))

# 3 — Abyss: nearly black depths with a single luminous ribbon of current.
defs = """<radialGradient id="bg" cx="0.5" cy="1.1" r="1.1">
  <stop offset="0" stop-color="#11283b"/><stop offset="0.6" stop-color="#0a131d"/><stop offset="1" stop-color="#05080d"/>
</radialGradient>
<linearGradient id="rib" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#6cc7e8" stop-opacity="0"/><stop offset="0.3" stop-color="#6cc7e8"/>
  <stop offset="0.7" stop-color="#9aaefa"/><stop offset="1" stop-color="#b7a2f0" stop-opacity="0"/>
</linearGradient>
<filter id="glow" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
<filter id="glow2" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>"""
body = f'<rect width="{W}" height="{H}" fill="url(#bg)"/>'
for k in range(14):
    comps = [(1.0, 0.75, 0.2 + k*0.05), (0.35, 1.6, 1.0 + k*0.11)]
    d = wave_line(1500 + k*14, 260 - k*6, comps, 0.4)
    op = 0.9 if k == 0 else 0.35 * (1 - k/14)
    body += f'<path d="{d}" fill="none" stroke="url(#rib)" stroke-width="{26 if k == 0 else 4}" opacity="{op:.2f}" filter="url(#glow)"/>'
    body += f'<path d="{d}" fill="none" stroke="url(#rib)" stroke-width="{3 if k == 0 else 1.5}" opacity="{min(1, op+0.2):.2f}" filter="url(#glow2)"/>'
open(f"{out}/3-abyss.svg", "w").write(svg(defs, body))

# 4 — Lagoon: dusk horizon over still water with a mirrored glow.
defs = """<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#070d18"/><stop offset="0.45" stop-color="#16213f"/>
  <stop offset="0.78" stop-color="#3a4c8c"/><stop offset="0.93" stop-color="#7fa6d6"/><stop offset="1" stop-color="#bfe4ef"/>
</linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#3b6f95"/><stop offset="0.25" stop-color="#173451"/><stop offset="1" stop-color="#070d16"/>
</linearGradient>
<radialGradient id="sun" cx="0.5" cy="0.61" r="0.35">
  <stop offset="0" stop-color="#e6f7ff" stop-opacity="0.9"/><stop offset="0.25" stop-color="#9fd7e6" stop-opacity="0.35"/><stop offset="1" stop-color="#9fd7e6" stop-opacity="0"/>
</radialGradient>
<filter id="b"><feGaussianBlur stdDeviation="6"/></filter>"""
hz = int(H * 0.61)
body = f'<rect width="{W}" height="{hz}" fill="url(#sky)"/><rect y="{hz}" width="{W}" height="{H-hz}" fill="url(#sea)"/>'
body += f'<rect width="{W}" height="{H}" fill="url(#sun)"/>'
for k in range(26):
    y = hz + 20 + (k ** 1.6) * 7
    w = 900 - k * 25
    body += f'<rect x="{W/2 - w/2:.0f}" y="{y:.0f}" width="{w}" height="{3 + k*0.4:.1f}" rx="2" fill="#dff4fb" opacity="{0.35*(1-k/26):.2f}" filter="url(#b)"/>'
body += f'<path d="{wave(hz-60, 40, [(1,1.2,0.4),(0.4,2.7,1.2)], 0)}" fill="#0b1626" opacity="0.0"/>'
# distant islands
body += f'<path d="M 0 {hz} C 400 {hz-90} 700 {hz-140} 1100 {hz-30} C 1250 {hz-10} 1350 {hz} 1500 {hz} Z" fill="#0c1628" opacity="0.95"/>'
body += f'<path d="M 2700 {hz} C 3000 {hz-60} 3300 {hz-110} 3840 {hz-70} L 3840 {hz} Z" fill="#0c1628" opacity="0.95"/>'
open(f"{out}/4-lagoon.svg", "w").write(svg(defs, body))
print("ok")
