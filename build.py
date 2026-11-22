#!/usr/bin/env python3
"""
Static Site Generator for Kunal Bhai Patel's Engineering & Maker Portfolio.
Builds a 100% static, hybrid multi-page bilingual (EN/DE) website with:
- Dedicated pages for Home, Projects, Research, About Me, Contact
- Reusable project case study detail pages
- Switchable Dark and Light themes with instant anti-FOUC initialization
- Strict path-preserving language switching
- Precision vector schematics and zero external dependencies
"""

import os
import json
import shutil
import glob
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
SRC_DIR = BASE_DIR / "src"
DIST_DIR = BASE_DIR / "dist"

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def get_base_prefix(depth=0):
    """Returns relative path prefix based on directory nesting depth."""
    if depth == 0:
        return "./"
    return "../" * depth

def render_hero_visual(lang="en"):
    """Generates an authentic, restrained isometric CAD & kinematics vector composition for the hero frame."""
    badge = "CAD KINEMATICS & PROBE ENVELOPE" if lang == "en" else "CAD-KINEMATIK & PRÜFFELD"
    sub = "PTC CREO / METROLOGY TEST RIG" if lang == "en" else "PTC CREO / PRÜFSTANDSAUFBAU"
    return f"""
    <svg class="schematic-svg" viewBox="0 0 540 338" xmlns="http://www.w3.org/2000/svg" aria-label="Isometric CAD and kinematics visual composition">
      <defs>
        <pattern id="hero-grid" width="18" height="18" patternUnits="userSpaceOnUse">
          <path d="M 18 0 L 0 0 0 18" fill="none" stroke="rgba(120, 150, 173, 0.08)" stroke-width="0.8"/>
        </pattern>
        <linearGradient id="hero-beam" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="rgba(120, 150, 173, 0.45)"/>
          <stop offset="100%" stop-color="rgba(120, 150, 173, 0.03)"/>
        </linearGradient>
      </defs>
      <rect width="540" height="338" fill="#11171e"/>
      <rect width="540" height="338" fill="url(#hero-grid)"/>

      <!-- Corner Crosshairs -->
      <path d="M 16 26 L 16 16 L 26 16" fill="none" stroke="#7896ad" stroke-width="1.5"/>
      <path d="M 524 26 L 524 16 L 514 16" fill="none" stroke="#7896ad" stroke-width="1.5"/>
      <path d="M 16 312 L 16 322 L 26 322" fill="none" stroke="#7896ad" stroke-width="1.5"/>
      <path d="M 524 312 L 524 322 L 514 322" fill="none" stroke="#7896ad" stroke-width="1.5"/>

      <!-- Isometric Calibrated Worktable Base -->
      <polygon points="120,240 280,290 440,240 280,190" fill="#18232e" stroke="#2a3b4a" stroke-width="1.5"/>
      <polygon points="120,240 280,290 280,305 120,255" fill="#141c24" stroke="#2a3b4a" stroke-width="1.5"/>
      <polygon points="280,290 440,240 440,255 280,305" fill="#19242f" stroke="#2a3b4a" stroke-width="1.5"/>

      <!-- Isometric Fixture Stage with Test Specimen -->
      <polygon points="220,225 280,245 340,225 280,205" fill="#1f2d3a" stroke="#7896ad" stroke-width="1.2"/>
      <ellipse cx="280" cy="225" rx="35" ry="14" fill="#17222c" stroke="#60a5fa" stroke-width="1.5"/>
      <circle cx="280" cy="225" r="3.5" fill="#fcd34d"/>

      <!-- Cobot Arm Flange & Inspection Probe Assembly -->
      <line x1="280" y1="50" x2="280" y2="105" stroke="#7896ad" stroke-width="8" stroke-linecap="round"/>
      <circle cx="280" cy="105" r="14" fill="#1c2834" stroke="#9bb8d1" stroke-width="2"/>
      <polygon points="255,120 305,120 295,155 265,155" fill="#202e3b" stroke="#9bb8d1" stroke-width="1.5"/>
      
      <!-- Directional Inspection Beam Cone -->
      <polygon points="265,155 295,155 320,225 240,225" fill="url(#hero-beam)"/>
      <line x1="280" y1="155" x2="280" y2="225" stroke="#60a5fa" stroke-width="1" stroke-dasharray="3 3"/>

      <!-- Precision Coordinate Axes Indicator -->
      <g transform="translate(55, 65)">
        <line x1="0" y1="0" x2="35" y2="12" stroke="#f3f4f2" stroke-width="1.5"/>
        <line x1="0" y1="0" x2="-25" y2="12" stroke="#f3f4f2" stroke-width="1.5"/>
        <line x1="0" y1="0" x2="0" y2="-32" stroke="#f3f4f2" stroke-width="1.5"/>
        <text x="38" y="16" fill="#f3f4f2" font-family="monospace" font-size="9">+X</text>
        <text x="-38" y="16" fill="#f3f4f2" font-family="monospace" font-size="9">+Y</text>
        <text x="-4" y="-36" fill="#f3f4f2" font-family="monospace" font-size="9">+Z</text>
      </g>

      <!-- Technical Annotations -->
      <text x="480" y="55" fill="#7896ad" font-family="monospace" font-size="9" text-anchor="end" letter-spacing="0.5">{badge}</text>
      <text x="480" y="70" fill="#6b7280" font-family="monospace" font-size="8" text-anchor="end">{sub}</text>

      <text x="280" y="270" fill="#9bb8d1" font-family="monospace" font-size="9" text-anchor="middle">~6 µm DEFECT RESOLUTION TARGET</text>
    </svg>
    """

def render_schematic(project_id, lang="en", is_detail=False):
    """Generates authentic, high-precision SVG technical engineering schematics with illustrative disclaimer."""
    view_box = "0 0 800 480" if is_detail else "0 0 600 375"
    w = 800 if is_detail else 600
    h = 480 if is_detail else 375

    grid_pattern = f"""
      <defs>
        <pattern id="grid-{project_id}-{is_detail}" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(120, 150, 173, 0.07)" stroke-width="0.8"/>
        </pattern>
        <linearGradient id="beam-grad-{project_id}" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="rgba(120, 150, 173, 0.45)"/>
          <stop offset="100%" stop-color="rgba(120, 150, 173, 0.05)"/>
        </linearGradient>
      </defs>
      <rect width="{w}" height="{h}" fill="#12181f"/>
      <rect width="{w}" height="{h}" fill="url(#grid-{project_id}-{is_detail})"/>
    """

    disclaimer = "ILLUSTRATIVE KINEMATIC CONCEPT" if lang == "en" else "ILLUSTRATIVES KINEMATIK-SCHEMA"

    if project_id == "rio-sio":
        lbl_cobot = "FANUC CR-7iA/L 6-AXIS COBOT"
        lbl_optics = "OPTICAL PROBE & COLLIMATED UV"
        lbl_target = "OPTICAL SPECIMEN (~6 µm RESOLUTION)"
        lbl_base = "OPTICAL ISOLATION BASEPLATE" if lang == "en" else "OPTISCHE GRUNDPLATTE"
        return f"""
        <svg class="schematic-svg" viewBox="{view_box}" xmlns="http://www.w3.org/2000/svg" aria-label="Rio sio kinematic and optical inspection schematic">
          {grid_pattern}
          <!-- Base Isolation Table -->
          <rect x="60" y="380" width="680" height="40" rx="3" fill="#18222b" stroke="#2c3c4a" stroke-width="1.5"/>
          <line x1="80" y1="420" x2="80" y2="455" stroke="#2c3c4a" stroke-width="4"/>
          <line x1="720" y1="420" x2="720" y2="455" stroke="#2c3c4a" stroke-width="4"/>
          <text x="400" y="405" fill="#7896ad" font-family="monospace" font-size="11" text-anchor="middle" letter-spacing="1.5">{lbl_base}</text>
          
          <!-- Robot Pedestal (J1) -->
          <rect x="140" y="290" width="90" height="90" rx="4" fill="#1b2733" stroke="#7896ad" stroke-width="1.5"/>
          <circle cx="185" cy="335" r="24" fill="#141c24" stroke="#7896ad" stroke-width="1.5"/>
          <text x="185" y="340" fill="#9bb8d1" font-family="monospace" font-size="10" text-anchor="middle">J1 (±360°)</text>

          <!-- Cobot Arm Link 1 & Shoulder (J2) -->
          <line x1="185" y1="290" x2="230" y2="180" stroke="#7896ad" stroke-width="8" stroke-linecap="round"/>
          <circle cx="230" cy="180" r="18" fill="#1b2733" stroke="#9bb8d1" stroke-width="2"/>
          <text x="230" y="184" fill="#f3f4f2" font-family="monospace" font-size="9" text-anchor="middle">J2</text>

          <!-- Cobot Arm Link 2 & Elbow (J3) -->
          <line x1="230" y1="180" x2="380" y2="130" stroke="#7896ad" stroke-width="7" stroke-linecap="round"/>
          <circle cx="380" cy="130" r="16" fill="#1b2733" stroke="#9bb8d1" stroke-width="2"/>
          <text x="380" y="134" fill="#f3f4f2" font-family="monospace" font-size="9" text-anchor="middle">J3</text>

          <!-- Forearm & Wrist (J4/J5/J6) -->
          <line x1="380" y1="130" x2="490" y2="175" stroke="#7896ad" stroke-width="6" stroke-linecap="round"/>
          <circle cx="490" cy="175" r="14" fill="#1b2733" stroke="#9bb8d1" stroke-width="2"/>

          <!-- End-Effector Inspection Tool Flange -->
          <rect x="480" y="195" width="70" height="55" rx="3" fill="#202e3b" stroke="#9bb8d1" stroke-width="1.5"/>
          <polygon points="495,250 535,250 525,275 505,275" fill="#7896ad" opacity="0.8"/>
          <text x="515" y="226" fill="#f3f4f2" font-family="monospace" font-size="9" text-anchor="middle">SENSOR</text>

          <!-- Collimated Beam Path (Directional Light Cone) -->
          <polygon points="505,275 525,275 570,360 460,360" fill="url(#beam-grad-rio-sio)"/>
          <line x1="515" y1="275" x2="515" y2="360" stroke="#9bb8d1" stroke-width="1.2" stroke-dasharray="3 3"/>

          <!-- Optical Specimen Stage & Fixture -->
          <rect x="430" y="360" width="170" height="20" rx="2" fill="#22313f" stroke="#7896ad" stroke-width="1.5"/>
          <path d="M 460 360 Q 515 350 570 360" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
          <circle cx="515" cy="355" r="4" fill="#fcd34d"/>
          
          <!-- Annotations & Dimension Labels -->
          <text x="270" y="80" fill="#9bb8d1" font-family="monospace" font-size="11" font-weight="600">{lbl_cobot}</text>
          <line x1="270" y1="88" x2="330" y2="135" stroke="#7896ad" stroke-width="1" stroke-dasharray="2 2"/>

          <text x="580" y="210" fill="#9bb8d1" font-family="monospace" font-size="10">{lbl_optics}</text>
          <line x1="575" y1="210" x2="555" y2="215" stroke="#7896ad" stroke-width="1"/>

          <text x="515" y="340" fill="#fcd34d" font-family="monospace" font-size="10" text-anchor="middle">{lbl_target}</text>

          <!-- Concept Disclaimer -->
          <text x="750" y="465" fill="#4b5563" font-family="monospace" font-size="8" text-anchor="end">{disclaimer}</text>

          <!-- Coordinate Frame -->
          <g transform="translate(80, 80)">
            <line x1="0" y1="0" x2="40" y2="0" stroke="#f3f4f2" stroke-width="1.5"/>
            <line x1="0" y1="0" x2="0" y2="-40" stroke="#f3f4f2" stroke-width="1.5"/>
            <text x="45" y="4" fill="#f3f4f2" font-family="monospace" font-size="10">+X</text>
            <text x="-4" y="-45" fill="#f3f4f2" font-family="monospace" font-size="10">+Z</text>
          </g>
        </svg>
        """

    elif project_id == "plottu":
        lbl_envelope = "A4 DRAWING ENVELOPE" if lang == "en" else "A4 ZEICHENBEREICH"
        lbl_servo = "SERVO PEN-LIFT (Z)" if lang == "en" else "SERVO-STIFTABHEBUNG (Z)"
        lbl_gantry = "Y-AXIS GANTRY BEAM" if lang == "en" else "Y-ACHSENQUERTRÄGER"
        return f"""
        <svg class="schematic-svg" viewBox="{view_box}" xmlns="http://www.w3.org/2000/svg" aria-label="Plottu Wi-Fi Pen Plotter Gantry Schematic">
          {grid_pattern}
          <!-- Outer Structural Frame / Gantry Extrusions -->
          <rect x="70" y="50" width="660" height="340" rx="4" fill="none" stroke="#283947" stroke-width="4"/>
          <rect x="75" y="55" width="650" height="330" rx="3" fill="#131b23" stroke="#1c2833" stroke-width="1"/>

          <!-- X-Axis Linear Rails -->
          <line x1="80" y1="90" x2="720" y2="90" stroke="#7896ad" stroke-width="3"/>
          <line x1="80" y1="350" x2="720" y2="350" stroke="#7896ad" stroke-width="3"/>

          <!-- Y-Axis Gantry Beam (Crossbar) -->
          <rect x="340" y="70" width="36" height="300" rx="3" fill="#1c2936" stroke="#9bb8d1" stroke-width="1.5"/>
          <line x1="358" y1="75" x2="358" y2="365" stroke="#7896ad" stroke-width="2"/>

          <!-- Pen Carriage with Micro-Servo -->
          <rect x="330" y="190" width="56" height="65" rx="3" fill="#243444" stroke="#60a5fa" stroke-width="1.5"/>
          <rect x="342" y="198" width="32" height="22" rx="2" fill="#17222d" stroke="#7896ad" stroke-width="1"/>
          <line x1="358" y1="220" x2="358" y2="245" stroke="#f3f4f2" stroke-width="3" stroke-linecap="round"/>
          <circle cx="358" cy="248" r="3" fill="#fcd34d"/>
          
          <!-- Drawing Paper Bed -->
          <rect x="180" y="120" width="290" height="200" fill="#18232e" stroke="#2f4252" stroke-dasharray="4 4"/>
          <text x="210" y="145" fill="#7896ad" font-family="monospace" font-size="10">{lbl_envelope}</text>

          <!-- Stepper Motor Blocks -->
          <rect x="85" y="65" width="40" height="40" rx="2" fill="#1e2c38" stroke="#7896ad" stroke-width="1.5"/>
          <text x="105" y="90" fill="#9bb8d1" font-family="monospace" font-size="9" text-anchor="middle">NEMA</text>
          
          <rect x="85" y="315" width="40" height="40" rx="2" fill="#1e2c38" stroke="#7896ad" stroke-width="1.5"/>
          <text x="105" y="340" fill="#9bb8d1" font-family="monospace" font-size="9" text-anchor="middle">NEMA</text>

          <!-- Controller Board (MKS TinyBee ESP32) -->
          <rect x="560" y="270" width="130" height="90" rx="3" fill="#1a2734" stroke="#7896ad" stroke-width="1.5"/>
          <text x="625" y="295" fill="#f3f4f2" font-family="monospace" font-size="10" text-anchor="middle">MKS TinyBee 1.0</text>
          <text x="625" y="315" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">ESP32 · FluidNC</text>
          <path d="M 615 335 A 8 8 0 0 1 635 335 M 618 340 A 5 5 0 0 1 632 340 M 625 344 L 625 345" fill="none" stroke="#60a5fa" stroke-width="1.5"/>

          <!-- Descriptive Annotations -->
          <text x="400" y="215" fill="#60a5fa" font-family="monospace" font-size="10">{lbl_servo}</text>
          <text x="358" y="55" fill="#9bb8d1" font-family="monospace" font-size="10" text-anchor="middle">{lbl_gantry}</text>
          <text x="400" y="415" fill="#7896ad" font-family="monospace" font-size="10" text-anchor="middle">GT2 BELT DRIVE · WIRELESS G-CODE STREAMING</text>
          <text x="750" y="465" fill="#4b5563" font-family="monospace" font-size="8" text-anchor="end">{disclaimer}</text>
        </svg>
        """

    elif project_id == "hdd-enclosure":
        return f"""
        <svg class="schematic-svg" viewBox="{view_box}" xmlns="http://www.w3.org/2000/svg" aria-label="Dual-HDD Enclosure Cooling Schematic">
          {grid_pattern}
          <rect x="120" y="80" width="560" height="280" rx="6" fill="#151f28" stroke="#7896ad" stroke-width="2"/>
          <rect x="230" y="110" width="300" height="90" rx="3" fill="#1c2833" stroke="#9bb8d1" stroke-width="1.5"/>
          <text x="380" y="150" fill="#f3f4f2" font-family="monospace" font-size="11" text-anchor="middle">3.5" SATA HDD — BAY 1</text>
          <circle cx="245" cy="125" r="4" fill="#fcd34d"/>
          <circle cx="515" cy="125" r="4" fill="#fcd34d"/>
          
          <rect x="230" y="230" width="300" height="90" rx="3" fill="#1c2833" stroke="#9bb8d1" stroke-width="1.5"/>
          <text x="380" y="270" fill="#f3f4f2" font-family="monospace" font-size="11" text-anchor="middle">3.5" SATA HDD — BAY 2</text>
          <circle cx="245" cy="245" r="4" fill="#fcd34d"/>
          <circle cx="515" cy="245" r="4" fill="#fcd34d"/>

          <rect x="140" y="145" width="60" height="150" rx="3" fill="#202e3b" stroke="#60a5fa" stroke-width="1.5"/>
          <circle cx="170" cy="220" r="28" fill="#151f28" stroke="#60a5fa" stroke-width="1.5"/>
          <text x="170" y="224" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">80mm FAN</text>

          <path d="M 210 150 L 550 150 M 540 145 L 550 150 L 540 155" fill="none" stroke="#60a5fa" stroke-width="1.8" stroke-dasharray="4 4"/>
          <path d="M 210 270 L 550 270 M 540 265 L 550 270 L 540 275" fill="none" stroke="#60a5fa" stroke-width="1.8" stroke-dasharray="4 4"/>
          
          <text x="400" y="390" fill="#7896ad" font-family="monospace" font-size="10" text-anchor="middle">M3/M4 HEAT-SET INSERTS · TPU VIBRATION ISOLATION</text>
          <text x="750" y="465" fill="#4b5563" font-family="monospace" font-size="8" text-anchor="end">{disclaimer}</text>
        </svg>
        """

    elif project_id == "home-server":
        return f"""
        <svg class="schematic-svg" viewBox="{view_box}" xmlns="http://www.w3.org/2000/svg" aria-label="Debian Home Server Architecture Schematic">
          {grid_pattern}
          <rect x="220" y="70" width="360" height="280" rx="6" fill="#16222c" stroke="#7896ad" stroke-width="2"/>
          <rect x="235" y="85" width="330" height="40" rx="3" fill="#1b2835" stroke="#9bb8d1" stroke-width="1"/>
          <text x="400" y="110" fill="#f3f4f2" font-family="monospace" font-size="12" text-anchor="middle">DEBIAN GNU/LINUX 12 (HEADLESS)</text>

          <rect x="250" y="145" width="300" height="50" rx="2" fill="#1c2a37" stroke="#7896ad" stroke-width="1"/>
          <text x="400" y="175" fill="#9bb8d1" font-family="monospace" font-size="10" text-anchor="middle">SECURE STORAGE POOL (SATA / EXT4)</text>

          <rect x="250" y="215" width="140" height="55" rx="3" fill="#202f3e" stroke="#60a5fa" stroke-width="1.2"/>
          <text x="320" y="247" fill="#f3f4f2" font-family="monospace" font-size="10" text-anchor="middle">NEXTCLOUD</text>
          
          <rect x="410" y="215" width="140" height="55" rx="3" fill="#202f3e" stroke="#60a5fa" stroke-width="1.2"/>
          <text x="480" y="247" fill="#f3f4f2" font-family="monospace" font-size="10" text-anchor="middle">JELLYFIN</text>

          <rect x="250" y="290" width="300" height="40" rx="2" fill="#17222c" stroke="#4ade80" stroke-width="1"/>
          <text x="400" y="315" fill="#4ade80" font-family="monospace" font-size="10" text-anchor="middle">TAILSCALE ENCRYPTED MESH (WIREGUARD)</text>

          <text x="400" y="390" fill="#7896ad" font-family="monospace" font-size="10" text-anchor="middle">ZERO INBOUND PORTS · PRIVATE OVERLAY ACCESS</text>
          <text x="750" y="465" fill="#4b5563" font-family="monospace" font-size="8" text-anchor="end">{disclaimer}</text>
        </svg>
        """

    elif project_id == "3d-printing":
        return f"""
        <svg class="schematic-svg" viewBox="{view_box}" xmlns="http://www.w3.org/2000/svg" aria-label="3D Printing & Fabrication Tuning Schematic">
          {grid_pattern}
          <rect x="360" y="70" width="80" height="90" rx="2" fill="#1e2b37" stroke="#7896ad" stroke-width="1.5"/>
          <text x="400" y="115" fill="#9bb8d1" font-family="monospace" font-size="9" text-anchor="middle">HEATSINK</text>

          <rect x="375" y="160" width="50" height="35" rx="1" fill="#2b3b4a" stroke="#fcd34d" stroke-width="1.5"/>
          <text x="400" y="182" fill="#fcd34d" font-family="monospace" font-size="8" text-anchor="middle">HEATER</text>

          <polygon points="388,195 412,195 403,215 397,215" fill="#fcd34d"/>
          <line x1="400" y1="215" x2="400" y2="235" stroke="#60a5fa" stroke-width="2"/>

          <g transform="translate(250, 235)">
            <rect x="0" y="0" width="300" height="15" rx="1" fill="#1d2a36" stroke="#60a5fa" stroke-width="0.8"/>
            <rect x="20" y="15" width="260" height="15" rx="1" fill="#1d2a36" stroke="#60a5fa" stroke-width="0.8"/>
            <rect x="40" y="30" width="220" height="15" rx="1" fill="#1d2a36" stroke="#60a5fa" stroke-width="0.8"/>
            <rect x="60" y="45" width="180" height="20" rx="1" fill="#1d2a36" stroke="#60a5fa" stroke-width="0.8"/>
          </g>

          <g transform="translate(560, 150)">
            <rect x="0" y="0" width="70" height="110" rx="2" fill="#1c2834" stroke="#7896ad" stroke-width="1.5"/>
            <rect x="15" y="20" width="40" height="60" fill="#fcd34d" stroke="#d97706" stroke-width="1"/>
            <text x="35" y="100" fill="#fcd34d" font-family="monospace" font-size="8" text-anchor="middle">M3 INSERT</text>
          </g>

          <text x="400" y="380" fill="#7896ad" font-family="monospace" font-size="10" text-anchor="middle">TOLERANCE OFFSETS (±0.2 mm) · HEAT-SET INSERT BOSS GEOMETRY</text>
          <text x="750" y="465" fill="#4b5563" font-family="monospace" font-size="8" text-anchor="end">{disclaimer}</text>
        </svg>
        """

    else: # local-ai
        return f"""
        <svg class="schematic-svg" viewBox="{view_box}" xmlns="http://www.w3.org/2000/svg" aria-label="Local AI Voice Pipeline Schematic">
          {grid_pattern}
          <rect x="70" y="150" width="110" height="90" rx="4" fill="#18232e" stroke="#7896ad" stroke-width="1.5"/>
          <circle cx="125" cy="185" r="16" fill="#1e2c38" stroke="#9bb8d1" stroke-width="1.2"/>
          <text x="125" y="222" fill="#f3f4f2" font-family="monospace" font-size="9" text-anchor="middle">MIC CAPTURE</text>

          <rect x="220" y="150" width="120" height="90" rx="4" fill="#18232e" stroke="#60a5fa" stroke-width="1.5"/>
          <text x="280" y="190" fill="#60a5fa" font-family="monospace" font-size="10" text-anchor="middle">WAKE WORD</text>
          <text x="280" y="210" fill="#9bb8d1" font-family="monospace" font-size="8" text-anchor="middle">LOCAL VAD</text>

          <rect x="380" y="130" width="160" height="130" rx="5" fill="#1d2a37" stroke="#4ade80" stroke-width="2"/>
          <text x="460" y="175" fill="#4ade80" font-family="monospace" font-size="11" font-weight="600" text-anchor="middle">OLLAMA ENGINE</text>
          <text x="460" y="200" fill="#f3f4f2" font-family="monospace" font-size="9" text-anchor="middle">3B–7B QUANTIZED</text>
          <text x="460" y="220" fill="#9bb8d1" font-family="monospace" font-size="8" text-anchor="middle">LOCAL MEMORY BOUND</text>

          <rect x="580" y="150" width="120" height="90" rx="4" fill="#18232e" stroke="#7896ad" stroke-width="1.5"/>
          <text x="640" y="190" fill="#f3f4f2" font-family="monospace" font-size="10" text-anchor="middle">LOCAL TTS</text>
          <text x="640" y="210" fill="#9bb8d1" font-family="monospace" font-size="8" text-anchor="middle">SYNTHESIS</text>

          <line x1="180" y1="195" x2="220" y2="195" stroke="#7896ad" stroke-width="2"/>
          <line x1="340" y1="195" x2="380" y2="195" stroke="#60a5fa" stroke-width="2"/>
          <line x1="540" y1="195" x2="580" y2="195" stroke="#4ade80" stroke-width="2"/>

          <text x="400" y="340" fill="#4ade80" font-family="monospace" font-size="10" text-anchor="middle">100% OFFLINE INFERENCE · ZERO CLOUD AUDIO TRANSMISSION</text>
          <text x="750" y="465" fill="#4b5563" font-family="monospace" font-size="8" text-anchor="end">{disclaimer}</text>
        </svg>
        """

def render_header(site, trans, lang, current_page, depth=0):
    pfx = get_base_prefix(depth)
    
    # Calculate counterpart language URL that strictly preserves the counterpart page
    if current_page == "home":
        en_url = f"{pfx}en/"
        de_url = f"{pfx}de/"
    elif current_page == "projects":
        en_url = f"{pfx}en/projects/"
        de_url = f"{pfx}de/projects/"
    elif current_page == "research":
        en_url = f"{pfx}en/research/"
        de_url = f"{pfx}de/research/"
    elif current_page == "about":
        en_url = f"{pfx}en/about/"
        de_url = f"{pfx}de/about/"
    elif current_page == "contact":
        en_url = f"{pfx}en/contact/"
        de_url = f"{pfx}de/contact/"
    elif current_page.startswith("project-"):
        project_id = current_page.replace("project-", "")
        en_url = f"{pfx}en/projects/{project_id}/"
        de_url = f"{pfx}de/projects/{project_id}/"
    else:
        en_url = f"{pfx}en/"
        de_url = f"{pfx}de/"

    en_active = "active" if lang == "en" else ""
    de_active = "active" if lang == "de" else ""

    nav = trans["nav"]
    home_url = f"{pfx}{lang}/"
    projects_url = f"{pfx}{lang}/projects/"
    research_url = f"{pfx}{lang}/research/"
    about_url = f"{pfx}{lang}/about/"
    contact_url = f"{pfx}{lang}/contact/"

    # Active states
    home_cls = "active" if current_page == "home" else ""
    projects_cls = "active" if (current_page == "projects" or current_page.startswith("project-")) else ""
    research_cls = "active" if current_page == "research" else ""
    about_cls = "active" if current_page == "about" else ""
    contact_cls = "active" if current_page == "contact" else ""

    theme_toggle_aria = nav.get("theme_toggle_aria", "Toggle light or dark theme")

    return f"""
    <header class="site-header">
      <div class="container header-inner">
        <a href="{home_url}" class="site-brand">
          <span class="brand-name">{site['author']['name']}</span>
          <span class="brand-tag">{site['tagline'][lang]}</span>
        </a>

        <nav aria-label="Main Navigation">
          <ul class="nav-links">
            <li><a href="{home_url}" class="{home_cls}" data-nav="home">{nav['home']}</a></li>
            <li><a href="{projects_url}" class="{projects_cls}" data-nav="projects">{nav['projects']}</a></li>
            <li><a href="{research_url}" class="{research_cls}" data-nav="research">{nav['research']}</a></li>
            <li><a href="{about_url}" class="{about_cls}" data-nav="about">{nav['about']}</a></li>
            <li><a href="{contact_url}" class="{contact_cls}" data-nav="contact">{nav['contact']}</a></li>
          </ul>
        </nav>

        <div class="header-actions">
          <!-- Switchable Light and Dark Themes Toggle -->
          <button id="themeToggle" class="theme-toggle-btn" aria-label="{theme_toggle_aria}" title="{theme_toggle_aria}">
            <span class="theme-icon-sun" aria-hidden="true">☀️</span>
            <span class="theme-icon-moon" aria-hidden="true">🌙</span>
          </button>

          <!-- Symmetrical Language Switcher -->
          <div class="lang-switcher" aria-label="Language selection">
            <a href="{en_url}" class="lang-btn {en_active}" data-lang="en">EN</a>
            <a href="{de_url}" class="lang-btn {de_active}" data-lang="de">DE</a>
          </div>

          <button id="mobileNavToggle" class="mobile-nav-toggle" aria-label="Toggle mobile menu" aria-expanded="false">☰</button>
        </div>
      </div>

      <!-- Mobile Navigation Drawer -->
      <div id="mobileDrawer" class="mobile-drawer" aria-label="Mobile Navigation">
        <ul class="mobile-drawer-links">
          <li><a href="{home_url}" class="{home_cls}">{nav['home']}</a></li>
          <li><a href="{projects_url}" class="{projects_cls}">{nav['projects']}</a></li>
          <li><a href="{research_url}" class="{research_cls}">{nav['research']}</a></li>
          <li><a href="{about_url}" class="{about_cls}">{nav['about']}</a></li>
          <li><a href="{contact_url}" class="{contact_cls}">{nav['contact']}</a></li>
        </ul>
        <div class="mobile-drawer-actions">
          <button id="mobileThemeToggle" class="theme-toggle-btn" aria-label="{theme_toggle_aria}">
            <span class="theme-icon-sun" aria-hidden="true">☀️</span>
            <span class="theme-icon-moon" aria-hidden="true">🌙</span>
          </button>
          <div class="lang-switcher" aria-label="Language selection">
            <a href="{en_url}" class="lang-btn {en_active}" data-lang="en">EN</a>
            <a href="{de_url}" class="lang-btn {de_active}" data-lang="de">DE</a>
          </div>
        </div>
      </div>
    </header>
    """

def render_footer(site, trans, lang, depth=0):
    pfx = get_base_prefix(depth)
    footer = trans["footer"]
    author = site["author"]
    home_url = f"{pfx}{lang}/"
    projects_url = f"{pfx}{lang}/projects/"
    research_url = f"{pfx}{lang}/research/"
    about_url = f"{pfx}{lang}/about/"
    contact_url = f"{pfx}{lang}/contact/"

    # Authorship & tech string
    attribution = footer.get("attribution", f"Created by {author['name']} · Built with HTML, CSS, JavaScript & Python")

    return f"""
    <footer class="site-footer">
      <div class="container">
        <div class="footer-grid">
          <div>
            <div class="footer-col-title">{author['name']}</div>
            <p class="footer-tagline">
              {site['tagline'][lang]}
            </p>
            <p class="footer-degrees">
              {author['degrees'][0]}<br>
              {author['degrees'][1]}
            </p>
          </div>

          <div>
            <div class="footer-col-title">{trans['nav']['projects']} & {trans['nav']['research']}</div>
            <ul class="footer-links">
              <li><a href="{projects_url}">{trans['featured_projects']['filter_professional']}</a></li>
              <li><a href="{projects_url}">{trans['featured_projects']['filter_personal']}</a></li>
              <li><a href="{research_url}">{trans['research_page']['title']}</a></li>
              <li><a href="https://doi.org/10.1117/12.3111698" target="_blank" rel="noopener noreferrer">SPIE Paper (DOI) ↗</a></li>
            </ul>
          </div>

          <div>
            <div class="footer-col-title">{trans['nav']['about']} & {trans['nav']['contact']}</div>
            <ul class="footer-links">
              <li><a href="{about_url}">{trans['nav']['about']}</a></li>
              <li><a href="{contact_url}">{trans['nav']['contact']}</a></li>
              <li><a href="{author['linkedin_url']}" target="_blank" rel="noopener noreferrer">LinkedIn Profile ↗</a></li>
              <li><a href="{author['youtube_url']}" target="_blank" rel="noopener noreferrer">YouTube: {author['youtube_channel']} ↗</a></li>
            </ul>
          </div>
        </div>

        <div class="footer-bottom">
          <div class="footer-attribution">{attribution}</div>
          <div class="footer-rights">{footer['rights']}</div>
          <div><a href="#top" id="backToTop" class="back-to-top-link">{footer['back_to_top']} ↑</a></div>
        </div>
      </div>
    </footer>
    """

def render_html_shell(title, description, lang, content, site, trans, current_page, depth=0):
    pfx = get_base_prefix(depth)
    header = render_header(site, trans, lang, current_page, depth)
    footer = render_footer(site, trans, lang, depth)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>{title} | {site['site_name']}</title>
  <meta name="description" content="{description}">
  
  <!-- Modern Favicon / Monogram Placeholder -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%23101418'/><text x='50' y='65' font-size='50' font-family='sans-serif' font-weight='bold' text-anchor='middle' fill='%237896AD'>KP</text></svg>">
  
  <!-- Instant Anti-FOUC Theme Initialization (Zero Flash) -->
  <script>
    (function() {{
      try {{
        var saved = localStorage.getItem('kunal_portfolio_theme');
        if (saved === 'light' || saved === 'dark') {{
          document.documentElement.setAttribute('data-theme', saved);
        }} else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {{
          document.documentElement.setAttribute('data-theme', 'light');
        }} else {{
          document.documentElement.setAttribute('data-theme', 'dark');
        }}
      }} catch (e) {{}}
    }})();
  </script>

  <!-- CSS Design System -->
  <link rel="stylesheet" href="{pfx}css/style.css">
</head>
<body id="top">
  {header}

  <main>
    {content}
  </main>

  {footer}

  <!-- Client Interaction Script -->
  <script src="{pfx}js/main.js"></script>
</body>
</html>
"""

def generate_homepage(site, trans, projects, lang):
    """Generates the hybrid homepage: focused hero, 50/50 pillars, small featured gallery, teaser highlights."""
    pfx = get_base_prefix(1)
    hero = trans["hero"]
    pillars = trans["pillars"]
    featured = trans["featured_projects"]
    author = site["author"]

    # Small featured project gallery (2 highlighted projects: Rio sio & Plottu)
    featured_list = [p for p in projects if p.get("featured", False)][:2]
    if not featured_list:
        featured_list = projects[:2]

    featured_cards_html = []
    for proj in featured_list:
        p_id = proj["id"]
        p_title = proj["title"][lang]
        p_desc = proj["one_liner"][lang]
        p_status = proj["status"][lang]
        p_tags = proj["tags"][:3]
        detail_url = f"{pfx}{lang}/projects/{p_id}/"

        tags_html = "".join([f'<span class="tag-pill">{t}</span>' for t in p_tags])
        if proj.get("image"):
            card_visual = f'<img src="{pfx}{proj["image"]}" alt="{p_title}" class="project-card-img" loading="lazy" />'
        else:
            card_visual = render_schematic(p_id, lang, is_detail=False)

        featured_cards_html.append(f"""
        <article class="project-card" data-category="{proj['category']}">
          <a href="{detail_url}" class="card-media" aria-label="{p_title}">
            {card_visual}
          </a>
          <div class="card-body">
            <div class="card-meta">
              <span class="card-category">{proj['category_label'][lang]}</span>
              <span class="project-status-badge">{p_status}</span>
            </div>
            <h3 class="card-title"><a href="{detail_url}">{p_title}</a></h3>
            <p class="card-desc">{p_desc}</p>
            <div class="card-tags">{tags_html}</div>
            <div style="margin-top: 1.25rem;">
              <a href="{detail_url}" class="btn btn-secondary btn-sm" style="width: 100%;">{featured['view_case_study']} →</a>
            </div>
          </div>
        </article>
        """)

    featured_cards_str = "\n".join(featured_cards_html)

    # Pillar micro-capability items
    prof_caps_html = "".join([f"""
      <div class="cap-item">
        <span class="cap-label">{c['label']}</span>
        <span class="cap-value">{c['value']}</span>
      </div>
    """ for c in pillars['professional_caps']])

    personal_caps_html = "".join([f"""
      <div class="cap-item">
        <span class="cap-label">{c['label']}</span>
        <span class="cap-value">{c['value']}</span>
      </div>
    """ for c in pillars['personal_caps']])

    # Credentials list
    credentials_html = "".join([f"<span>{cr}</span>" for cr in hero.get("credentials", [])])

    content = f"""
    <!-- Refined Hero Section with 2-Column Composition -->
    <section class="hero-section" id="hero">
      <div class="container">
        <div class="hero-grid">
          <!-- Left Column: Headline, Concise Narrative, CTAs -->
          <div class="hero-content">
            <div class="hero-pill">
              <span style="display:inline-block; width:7px; height:7px; border-radius:50%; background:var(--accent-steel);"></span>
              {hero['pill']}
            </div>
            <h1 class="hero-title">{hero['title']}</h1>
            <p class="hero-lead">{hero['lead']}</p>
            <div class="hero-ctas">
              <a href="{pfx}{lang}/projects/" class="btn btn-primary">{hero['cta_projects']}</a>
              <a href="{pfx}{lang}/research/" class="btn btn-secondary">{hero['cta_research']}</a>
              <a href="{pfx}{lang}/about/" class="btn btn-outline">{hero['cta_about']}</a>
            </div>
            <div class="hero-credentials">
              {credentials_html}
            </div>
          </div>

          <!-- Right Column: Authentic Engineering Display Viewport -->
          <div class="hero-visual">
            <div class="hero-visual-frame">
              <div class="hero-visual-header">
                <div class="hero-visual-dots">
                  <div class="hero-visual-dot"></div>
                  <div class="hero-visual-dot"></div>
                  <div class="hero-visual-dot"></div>
                </div>
                <span>{hero['visual_badge']}</span>
              </div>
              <div class="hero-visual-inner">
                {render_hero_visual(lang)}
              </div>
              <div class="hero-visual-caption">
                <span style="color: var(--text-secondary);">{hero['visual_caption_title']}</span>
                <span>{hero['visual_caption_sub']}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Two Balanced Pillars Section (Equal 50/50 Prominence) -->
    <section class="section" id="pillars">
      <div class="container">
        <div class="section-header">
          <span class="section-badge">{pillars['section_title']}</span>
          <h2>Professional Precision · Workshop Curiosity</h2>
          <p class="section-desc">{pillars['section_desc']}</p>
        </div>

        <div class="pillars-grid">
          <!-- Pillar 1: Professional Engineering & Research -->
          <div class="pillar-card">
            <div class="pillar-header-group">
              <span class="pillar-badge">{pillars['professional_badge']}</span>
              <span class="pillar-index">01</span>
            </div>
            <h3 class="pillar-title">{pillars['professional_title']}</h3>
            <p class="pillar-lead">{pillars['professional_lead']}</p>
            
            <div class="pillar-capabilities">
              {prof_caps_html}
            </div>

            <div>
              <a href="{pfx}{lang}/research/" class="btn btn-secondary btn-sm">{pillars['cta_professional']}</a>
            </div>
          </div>

          <!-- Pillar 2: Workshop & Maker Projects -->
          <div class="pillar-card">
            <div class="pillar-header-group">
              <span class="pillar-badge">{pillars['personal_badge']}</span>
              <span class="pillar-index">02</span>
            </div>
            <h3 class="pillar-title">{pillars['personal_title']}</h3>
            <p class="pillar-lead">{pillars['personal_lead']}</p>
            
            <div class="pillar-capabilities">
              {personal_caps_html}
            </div>

            <div>
              <a href="{pfx}{lang}/projects/" class="btn btn-secondary btn-sm">{pillars['cta_personal']}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Small Featured Projects Preview -->
    <section class="section" id="featured-projects">
      <div class="container">
        <div class="section-header">
          <span class="section-badge">{featured['section_title']}</span>
          <h2>Featured Engineering Works</h2>
          <p class="section-desc">{featured['section_desc']}</p>
        </div>

        <div class="projects-grid">
          {featured_cards_str}
        </div>

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="{pfx}{lang}/projects/" class="btn btn-primary">
            {featured['view_all_cta']}
          </a>
        </div>
      </div>
    </section>

    <!-- Brief Research Highlight Teaser -->
    <section class="section" id="research-teaser">
      <div class="container">
        <div class="research-highlight-box">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 1rem; margin-bottom: 0.75rem;">
            <h3 style="font-size: 1.35rem; color: var(--text-primary);">{trans['research_page']['paper_title']}</h3>
            <span class="project-status-badge">{trans['research_page']['paper_badge']}</span>
          </div>
          <p style="color: var(--text-secondary); margin-bottom: 1.25rem; font-size: 0.95rem;">
            {trans['research_page']['lead']}
          </p>
          <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center;">
            <a href="{pfx}{lang}/research/" class="btn btn-secondary btn-sm">
              {trans['research_page']['title']} →
            </a>
            <a href="https://doi.org/10.1117/12.3111698" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
              SPIE Paper (DOI: 10.1117/12.3111698) ↗
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Connect & Contact CTA -->
    <section class="section" id="contact-teaser">
      <div class="container container-narrow" style="text-align: center;">
        <span class="section-badge">{trans['contact_page']['badge']}</span>
        <h2 style="margin-bottom: 1rem;">{trans['contact_page']['title']}</h2>
        <p style="font-size: 1.08rem; color: var(--text-secondary); margin-bottom: 2rem;">
          {trans['contact_page']['lead']}
        </p>
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 1rem;">
          <a href="{pfx}{lang}/contact/" class="btn btn-primary">
            {trans['nav']['contact']} →
          </a>
          <a href="{author['linkedin_url']}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
            LinkedIn Profile ↗
          </a>
        </div>
      </div>
    </section>
    """

    return render_html_shell(
        title=f"{author['name']} — {hero['title']}",
        description=hero['lead'],
        lang=lang,
        content=content,
        site=site,
        trans=trans,
        current_page="home",
        depth=1
    )

def generate_projects_page(site, trans, projects, lang):
    """Generates the dedicated Projects page with complete filterable gallery."""
    pfx = get_base_prefix(2)
    p_trans = trans["projects_page"]
    author = site["author"]

    project_cards_html = []
    for proj in projects:
        cat = proj["category"]
        p_id = proj["id"]
        p_title = proj["title"][lang]
        p_desc = proj["one_liner"][lang]
        p_status = proj["status"][lang]
        p_tags = proj["tags"][:4]
        
        detail_url = f"{pfx}{lang}/projects/{p_id}/"
        tags_html = "".join([f'<span class="tag-pill">{t}</span>' for t in p_tags])
        if proj.get("image"):
            card_visual = f'<img src="{pfx}{proj["image"]}" alt="{p_title}" class="project-card-img" loading="lazy" />'
        else:
            card_visual = render_schematic(p_id, lang, is_detail=False)

        project_cards_html.append(f"""
        <article class="project-card" data-category="{cat}">
          <a href="{detail_url}" class="card-media" aria-label="{p_title}">
            {card_visual}
          </a>
          <div class="card-body">
            <div class="card-meta">
              <span class="card-category">{proj['category_label'][lang]}</span>
              <span class="project-status-badge">{p_status}</span>
            </div>
            <h3 class="card-title"><a href="{detail_url}">{p_title}</a></h3>
            <p class="card-desc">{p_desc}</p>
            <div class="card-tags">{tags_html}</div>
            <div style="margin-top: 1.25rem;">
              <a href="{detail_url}" class="btn btn-secondary btn-sm" style="width: 100%;">{trans['featured_projects']['view_case_study']} →</a>
            </div>
          </div>
        </article>
        """)

    all_cards = "\n".join(project_cards_html)

    content = f"""
    <!-- Dedicated Projects Header -->
    <header class="page-header">
      <div class="container">
        <span class="page-badge">{p_trans['badge']}</span>
        <h1 class="page-title">{p_trans['title']}</h1>
        <p class="page-lead">{p_trans['lead']}</p>
      </div>
    </header>

    <!-- Projects Gallery Section -->
    <section class="section">
      <div class="container">
        <!-- Filter Bar -->
        <div class="filter-bar" role="tablist" aria-label="Project filter options">
          <button class="filter-btn active" data-filter="all" role="tab" aria-selected="true">{p_trans['filter_all']}</button>
          <button class="filter-btn" data-filter="professional" role="tab" aria-selected="false">{p_trans['filter_professional']}</button>
          <button class="filter-btn" data-filter="personal" role="tab" aria-selected="false">{p_trans['filter_personal']}</button>
        </div>

        <!-- Cards Grid -->
        <div class="projects-grid">
          {all_cards}
        </div>
      </div>
    </section>
    """

    return render_html_shell(
        title=f"{p_trans['title']} | {author['name']}",
        description=p_trans['lead'],
        lang=lang,
        content=content,
        site=site,
        trans=trans,
        current_page="projects",
        depth=2
    )

def generate_research_page(site, trans, lang):
    """Generates the dedicated Research page with in-depth metrology and SPIE paper details."""
    pfx = get_base_prefix(2)
    r_trans = trans["research_page"]
    author = site["author"]
    sections = r_trans["sections"]

    # Localized metadata items
    if lang == "de":
        meta_items = [
            ("Nachweisgrenze", "~6 µm Fehlergröße (nachgewiesen)"),
            ("Roboterplattform", "FANUC CR-7iA/L 6-Achs-Cobot"),
            ("Forschungseinrichtung", "TC Teisnach Optik / TH Deggendorf"),
            ("Förderprogramm", "IGF Vorhaben 01IF22263N")
        ]
    else:
        meta_items = [
            ("Detection Limit", "~6 µm Imperfection Resolution"),
            ("Cobot Platform", "FANUC CR-7iA/L 6-Axis Cobot"),
            ("Research Facility", "TC Teisnach Optik / TH Deggendorf"),
            ("Funding Program", "IGF Project 01IF22263N")
        ]

    research_meta_grid_html = "".join([f"""
      <div class="research-meta-item">
        <span class="research-meta-label">{m[0]}</span>
        <span class="research-meta-value">{m[1]}</span>
      </div>
    """ for m in meta_items])

    schematic_svg = render_schematic("rio-sio", lang, is_detail=True)

    content = f"""
    <!-- Dedicated Research Header -->
    <header class="page-header">
      <div class="container">
        <span class="page-badge">{r_trans['badge']}</span>
        <h1 class="page-title">{r_trans['title']}</h1>
        <p class="page-lead">{r_trans['lead']}</p>
      </div>
    </header>

    <!-- Research Main Content -->
    <section class="section">
      <div class="container">
        <!-- Official SPIE Publication Feature Box -->
        <div class="research-highlight-box" style="margin-bottom: 3rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 1rem; margin-bottom: 0.75rem;">
            <h2 style="font-size: 1.4rem; color: var(--text-primary);">{r_trans['paper_title']}</h2>
            <span class="project-status-badge">{r_trans['paper_badge']}</span>
          </div>
          <p style="color: var(--text-secondary); margin-bottom: 1.25rem; font-family: var(--font-mono); font-size: 0.88rem;">
            {r_trans['paper_venue']} · DOI: 10.1117/12.3111698
          </p>

          <div class="research-meta-grid">
            {research_meta_grid_html}
          </div>

          <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; margin-top: 1.5rem;">
            <a href="{r_trans['paper_doi_url']}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
              📄 {r_trans['paper_doi_label']} ↗
            </a>
            <span class="btn btn-outline btn-sm btn-disabled" title="{r_trans['thesis_note']}">
              📄 {r_trans['thesis_title']} ({r_trans['thesis_status']})
            </span>
            <a href="{pfx}{lang}/projects/rio-sio/" class="btn btn-secondary btn-sm">
              {r_trans['view_case_study']}
            </a>
          </div>
        </div>

        <!-- Technical Breakdown Columns -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; margin-bottom: 3rem;">
          <div>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.75rem; color: var(--text-primary);">
              01. {sections['challenge_title']}
            </h3>
            <p style="color: var(--text-secondary); line-height: 1.68; margin-bottom: 2rem;">
              {sections['challenge_text']}
            </p>

            <h3 style="font-size: 1.2rem; margin-bottom: 0.75rem; color: var(--text-primary);">
              02. {sections['robotics_title']}
            </h3>
            <p style="color: var(--text-secondary); line-height: 1.68;">
              {sections['robotics_text']}
            </p>
          </div>

          <div>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.75rem; color: var(--text-primary);">
              03. {sections['optics_title']}
            </h3>
            <p style="color: var(--text-secondary); line-height: 1.68; margin-bottom: 2rem;">
              {sections['optics_text']}
            </p>

            <h3 style="font-size: 1.2rem; margin-bottom: 0.75rem; color: var(--text-primary);">
              04. {sections['cad_title']}
            </h3>
            <p style="color: var(--text-secondary); line-height: 1.68;">
              {sections['cad_text']}
            </p>
          </div>
        </div>

        <!-- Research Rig & Laboratory Showcase -->
        <div class="research-rig-showcase">
          <div class="detail-schematic-container">
            {schematic_svg}
            <div class="schematic-caption">
              <span>FANUC CR-7iA/L Robotic Optical Inspection Test Rig</span>
              <span>Vector Schematic · DOI: 10.1117/12.3111698</span>
            </div>
          </div>
          <div class="research-photo-showcase">
            <div class="research-photo-wrap">
              <img src="{pfx}media/research/rio-sio/rio_sio_card.jpg" alt="Kunal Bhai Patel with FANUC CR-7iA/L robot test rig" loading="lazy" />
            </div>
            <div class="research-photo-desc">
              <p>
                {"Experimental cobotic metrology cell at TC Teisnach Optik: FANUC CR-7iA/L collaborative arm equipped with custom collimated dark-field illumination." if lang == "en" else "Kollaborative Messzelle am TC Teisnach Optik: FANUC CR-7iA/L Cobot mit eigens entwickelter kollimierter Dunkelfeldbeleuchtung."}
              </p>
              <a href="{pfx}{lang}/projects/rio-sio/" class="btn btn-secondary btn-sm">
                {r_trans['view_case_study']}
              </a>
            </div>
          </div>
        </div>

        <!-- Results & Conclusion Box -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 2rem;">
          <h3 style="font-size: 1.2rem; margin-bottom: 0.75rem; color: var(--text-primary);">
            05. {sections['results_title']}
          </h3>
          <p style="color: var(--text-secondary); line-height: 1.68; margin-bottom: 1.5rem;">
            {sections['results_text']}
          </p>
          <div>
            <a href="{pfx}{lang}/projects/rio-sio/" class="btn btn-secondary">
              {r_trans['view_case_study']}
            </a>
          </div>
        </div>
      </div>
    </section>
    """

    return render_html_shell(
        title=f"{r_trans['title']} | {author['name']}",
        description=r_trans['lead'],
        lang=lang,
        content=content,
        site=site,
        trans=trans,
        current_page="research",
        depth=2
    )

def generate_about_page(site, trans, lang):
    """Generates the dedicated About Me page with the approved personal story chapters and hero photograph."""
    pfx = get_base_prefix(2)
    a_trans = trans["about_page"]
    author = site["author"]

    # Editorial Chapters HTML
    chapters_html = []
    for ch in a_trans.get("chapters", []):
        paras_html = "".join([f"<p>{p.replace('{pfx}', pfx).replace('{lang}', lang)}</p>" for p in ch["paragraphs"]])
        chapters_html.append(f"""
        <article class="about-chapter">
          <span class="about-chapter-num">{ch['kicker']}</span>
          <h2 class="about-chapter-title">{ch['title']}</h2>
          <div class="about-prose">
            {paras_html}
          </div>
        </article>
        """)
    all_chapters_str = "\n".join(chapters_html)

    # Milestones Timeline
    milestones_html = "".join([f"""
      <div class="about-milestone-item">
        <span class="about-milestone-period">{m['period']}</span>
        <div class="about-milestone-title">{m['title']}</div>
        <div class="about-milestone-sub">{m['sub']}</div>
      </div>
    """ for m in a_trans.get("milestones", [])])

    # Competencies table localized
    if lang == "de":
        comp_rows = [
            ("CAD & Konstruktion", "PTC Creo Parametric, SolidWorks, Zeichnungserstellung"),
            ("Robotik & Steuerung", "FANUC CR-7iA/L, Siemens PCS 7 (Bedienung), FluidNC"),
            ("Berechnung & Code", "ANSYS, MATLAB, Python (Automatisierungsskripte)"),
            ("Fertigungstechnik", "FDM-3D-Druck, Toleranzprüfung, mechanischer Aufbau"),
            ("Sprachen", "Deutsch (sehr gut / Goethe B2), Englisch (fließend)")
        ]
    else:
        comp_rows = [
            ("CAD / Modeling", "PTC Creo Parametric, SolidWorks, Technical Drawings"),
            ("Robotics / Control", "FANUC CR-7iA/L, Siemens PCS 7 (Operation), FluidNC"),
            ("Analysis / Code", "ANSYS, MATLAB, Python (Applied automation)"),
            ("Fabrication", "FDM / 3D Printing, Calibration, Physical Commissioning"),
            ("Languages", "English (Fluent), German (Goethe B2 / Professional)")
        ]

    comp_table_html = "".join([f"""
      <tr>
        <td class="spec-key">{r[0]}</td>
        <td class="spec-val">{r[1]}</td>
      </tr>
    """ for r in comp_rows])

    content = f"""
    <!-- Dedicated About Header -->
    <header class="page-header">
      <div class="container">
        <span class="page-badge">{a_trans['badge']}</span>
        <h1 class="page-title">{a_trans['title']}</h1>
        <p class="page-lead">{a_trans['lead']}</p>
      </div>
    </header>

    <!-- About Main Content -->
    <section class="section">
      <div class="container">
        <!-- Hero Introduction: Headline on Left, Selected Photograph on Right -->
        <div class="about-hero-grid">
          <div class="about-hero-content">
            <span class="section-badge" style="margin-bottom: 0.75rem;">{a_trans['badge']}</span>
            <h2 class="about-hero-headline">{a_trans['hero_headline']}</h2>
            <p class="about-hero-subtitle">{a_trans['hero_subtitle']}</p>
            <p style="color: var(--text-secondary); line-height: 1.72; font-size: 1.05rem; margin-bottom: 1.5rem;">
              {"My fascination with engineering began long before I knew what an engineer actually did. From taking apart toy cars to explore their motors, to programming collaborative robots and custom kinematics in Bavaria." if lang == "en" else "Meine Begeisterung für Technik begann schon lange bevor ich überhaupt wusste, was ein Ingenieur macht. Vom Zerlegen kleiner Spielzeugautos bis zum Bau robotergestützter Prüfsysteme und eigener Bewegungssteuerungen in Bayern."}
            </p>
            <div style="display: flex; gap: 0.85rem; flex-wrap: wrap;">
              <a href="{pfx}{lang}/projects/rio-sio/" class="btn btn-primary btn-sm">
                {"Explore Rio sio Research Project →" if lang == "en" else "Rio sio Forschungsprojekt erkunden →"}
              </a>
              <a href="{pfx}{lang}/projects/" class="btn btn-secondary btn-sm">
                {"Workshop Projects →" if lang == "en" else "Werkstattprojekte →"}
              </a>
            </div>
          </div>

          <figure class="about-hero-photo-wrapper">
            <img src="{pfx}media/portrait/kunal_patel_about.jpg" alt="Kunal Bhai Patel — Mechanical & Mechatronics Engineer" loading="eager" width="1400" height="933" />
            <figcaption>
              <span>{a_trans['hero_caption']}</span>
            </figcaption>
          </figure>
        </div>

        <div class="detail-layout">
          <!-- Main Narrative Column: 4 Editorial Chapters -->
          <div class="detail-main">
            {all_chapters_str}

            <!-- Required "About This Website" Section -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-medium); border-left: 4px solid var(--accent-steel); border-radius: var(--radius-md); padding: 1.75rem; margin-top: 2.5rem;">
              <h3 style="font-size: 1.2rem; margin-bottom: 0.75rem; color: var(--text-primary);">
                🌐 {a_trans['website_section']['title']}
              </h3>
              <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.94rem;">
                {a_trans['website_section']['text']}
              </p>
            </div>
          </div>

          <!-- Sidebar Column: Milestones Timeline, Competencies, and Inquiries -->
          <aside class="detail-sidebar">
            <!-- Milestones Timeline Box -->
            <div class="sidebar-box">
              <div class="sidebar-box-title">{a_trans['milestones_title']}</div>
              <div class="about-milestone-list">
                {milestones_html}
              </div>
            </div>

            <!-- Technical Competencies Table -->
            <div class="sidebar-box">
              <div class="sidebar-box-title">{a_trans['competencies_title']}</div>
              <table class="specs-table">
                <tbody>
                  {comp_table_html}
                </tbody>
              </table>
            </div>

            <!-- Featured Case Study Card -->
            <div class="sidebar-box" style="border-left: 3px solid var(--accent-steel);">
              <div class="sidebar-box-title">{a_trans['case_study_card_title']}</div>
              <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
                {a_trans['case_study_card_text']}
              </p>
              <a href="{pfx}{lang}/projects/rio-sio/" class="btn btn-secondary btn-sm" style="width: 100%;">
                {a_trans['case_study_card_cta']}
              </a>
            </div>

            <!-- Location & Contact Box -->
            <div class="sidebar-box">
              <div class="sidebar-box-title">Location & Contact</div>
              <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1rem;">
                {"Based in Deggendorf / Bavaria, Germany.<br>Available for engineering opportunities and collaborations." if lang == "en" else "Wohnhaft in Deggendorf / Bayern, Deutschland.<br>Offen für ingenieurtechnische Aufgaben und Kooperationen."}
              </p>
              <a href="{pfx}{lang}/contact/" class="btn btn-primary btn-sm" style="width: 100%;">
                {trans['nav']['contact']} →
              </a>
            </div>
          </aside>
        </div>
      </div>
    </section>
    """

    return render_html_shell(
        title=f"{a_trans['title']} | {author['name']}",
        description=a_trans['lead'],
        lang=lang,
        content=content,
        site=site,
        trans=trans,
        current_page="about",
        depth=2
    )

def generate_contact_page(site, trans, lang):
    """Generates the dedicated Contact page with clear direct channels."""
    pfx = get_base_prefix(2)
    c_trans = trans["contact_page"]
    author = site["author"]

    content = f"""
    <!-- Dedicated Contact Header -->
    <header class="page-header">
      <div class="container">
        <span class="page-badge">{c_trans['badge']}</span>
        <h1 class="page-title">{c_trans['title']}</h1>
        <p class="page-lead">{c_trans['lead']}</p>
      </div>
    </header>

    <!-- Contact Cards Grid -->
    <section class="section">
      <div class="container">
        <div class="contact-grid">
          <!-- Card 1: LinkedIn Profile -->
          <div class="contact-card">
            <h3 class="contact-card-title">{c_trans['linkedin_card_title']}</h3>
            <p class="contact-card-text">{c_trans['linkedin_card_text']}</p>
            <div>
              <a href="{author['linkedin_url']}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="width: 100%;">
                {c_trans['linkedin_cta']}
              </a>
            </div>
          </div>

          <!-- Card 2: Professional Inquiries -->
          <div class="contact-card">
            <h3 class="contact-card-title">{c_trans['email_card_title']}</h3>
            <p class="contact-card-text">{c_trans['email_card_text']}</p>
            <div>
              <a href="{author['linkedin_url']}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="width: 100%;">
                {c_trans['email_cta']}
              </a>
            </div>
          </div>

          <!-- Card 3: Curriculum Vitae -->
          <div class="contact-card">
            <h3 class="contact-card-title">{c_trans['cv_card_title']}</h3>
            <p class="contact-card-text">{c_trans['cv_card_text']}</p>
            <div>
              <a href="{author['linkedin_url']}" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm" style="width: 100%;">
                {c_trans['cv_cta']}
              </a>
            </div>
          </div>

          <!-- Card 4: YouTube Channel -->
          <div class="contact-card">
            <h3 class="contact-card-title">{c_trans['youtube_card_title']}</h3>
            <p class="contact-card-text">{c_trans['youtube_card_text']}</p>
            <div>
              <a href="{author['youtube_url']}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="width: 100%;">
                {c_trans['youtube_cta']}
              </a>
            </div>
          </div>
        </div>

        <!-- Privacy & Static Hosting Notice -->
        <div style="text-align: center; margin-top: 3rem; padding: 1.5rem; background: var(--bg-surface-subtle); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); max-width: 680px; margin-left: auto; margin-right: auto;">
          <p style="font-family: var(--font-mono); font-size: 0.78rem; color: var(--text-muted);">
            {c_trans['notice']}
          </p>
        </div>
      </div>
    </section>
    """

    return render_html_shell(
        title=f"{c_trans['title']} | {author['name']}",
        description=c_trans['lead'],
        lang=lang,
        content=content,
        site=site,
        trans=trans,
        current_page="contact",
        depth=2
    )

def generate_rio_sio_detail(site, trans, project, lang):
    """Generates the comprehensive, rich Rio sio research case study with all 12 sections, 3 videos, real laboratory photographs, and metrics."""
    pfx = get_base_prefix(3)
    c = trans.get("rio_sio_case_study", {})
    p_tmpl = trans["project_template"]
    p_title = project["title"][lang]
    p_oneliner = project["one_liner"][lang]
    
    # Hero tags
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in c["meta"]["tags"]])

    content = f"""
    <div class="container" style="padding-top: 1.5rem; padding-bottom: 0.5rem;">
      <a href="{pfx}{lang}/projects/" class="back-link">{p_tmpl['back_to_projects']}</a>
    </div>

    <!-- 00. Hero Section -->
    <header class="hero" id="overview">
      <div class="container herogrid">
        <div>
          <span class="kicker">{c['meta']['kicker']}</span>
          <h1 style="font-size: clamp(2.3rem, 4.2vw, 3.6rem); line-height: 1.15; margin: 0.75rem 0 1.25rem;">{c['meta']['title']}</h1>
          <p class="lead" style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.65; max-width: 620px;">{c['meta']['lead']}</p>
          <div class="tags">
            {tags_html}
          </div>
          <div class="actions">
            <a class="btn btn-primary" href="#story">{c['meta']['cta_explore']}</a>
            <a class="btn btn-secondary" href="#publication">{c['meta']['cta_publication']}</a>
          </div>
        </div>
        <figure class="rio-hero-photo">
          <img alt="{c['meta']['hero_caption']}" loading="eager" src="{pfx}media/research/rio-sio/20250506_175617.jpg" />
          <figcaption>{c['meta']['hero_caption']}</figcaption>
        </figure>
      </div>

      <!-- Compact Recruiter Project Overview Card -->
      <div class="container" style="margin-top: 2.25rem;">
        <div class="rio-overview-card">
          <div class="rio-overview-header">
            <span class="rio-overview-badge">{"Research & Development Project Brief" if lang == "en" else "Forschungsprojekt im Überblick"}</span>
            <span class="rio-overview-meta">{"Master's Thesis Research · TH Deggendorf" if lang == "en" else "Master-Forschungsarbeit · TH Deggendorf"}</span>
          </div>
          <div class="rio-overview-grid">
            <div class="rio-overview-item">
              <span class="rio-overview-label">{"Research Institution" if lang == "en" else "Forschungsinstitut"}</span>
              <span class="rio-overview-val">Technologie Campus Teisnach Optik, TH Deggendorf</span>
            </div>
            <div class="rio-overview-item">
              <span class="rio-overview-label">{"Research Focus" if lang == "en" else "Forschungsschwerpunkt"}</span>
              <span class="rio-overview-val">{"Automated inspection of imperfections on optical surfaces" if lang == "en" else "Automatisierte Inspektion von Unvollkommenheiten auf optischen Oberflächen"}</span>
            </div>
            <div class="rio-overview-item">
              <span class="rio-overview-label">{"Core Technologies" if lang == "en" else "Kerntechnologien"}</span>
              <span class="rio-overview-val">{"FANUC CR-7iA/L, mechanical design, optical metrology, high-resolution imaging and controlled illumination" if lang == "en" else "FANUC CR-7iA/L, CAD-Konstruktion, optische Messtechnik, hochauflösende Bildgebung und kontrollierte Beleuchtung"}</span>
            </div>
            <div class="rio-overview-item">
              <span class="rio-overview-label">{"My Contributions" if lang == "en" else "Eigene Ingenieurbeiträge"}</span>
              <span class="rio-overview-val">{"CAD, mechanical and optomechanical integration, optical alignment, illumination experiments, robotic positioning, manual calibration and experimental validation" if lang == "en" else "CAD, mechanische und optomechatronische Integration, optische Justage, Beleuchtungsexperimente, Roboterkinematik, manuelle Kalibrierung und experimentelle Validierung"}</span>
            </div>
            <div class="rio-overview-item rio-overview-span">
              <span class="rio-overview-label">{"Research Outcome" if lang == "en" else "Forschungsergebnis & Validierung"}</span>
              <span class="rio-overview-val">{"Microscopic surface-defect inspection (~6 µm), experimental prototype and co-authored publication in SPIE Proceedings (DOI: 10.1117/12.3111698)" if lang == "en" else "Mikroskopische Oberflächendefekterkennung (~6 µm), Versuchsprototyp und Co-Autorenschaft in den SPIE Proceedings (DOI: 10.1117/12.3111698)"}</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- 00b. System Demonstration Video -->
    <section class="panel" id="demo">
      <div class="container">
        <div class="sectionhead" style="text-align: center; max-width: 820px; margin: 0 auto 1.5rem;">
          <span class="num">{c['demo']['num']}</span>
          <h2>{c['demo']['title']}</h2>
          <p class="video-intro" style="margin: 0.5rem auto 0;">{c['demo']['intro']}</p>
        </div>
        <figure class="video-showcase" id="video1">
          <div class="video-frame">
            <video class="autoplay-when-visible" controls loop muted playsinline preload="metadata" poster="{pfx}media/research/rio-sio/system_demo_poster.jpg" aria-label="{c['demo']['video_title']}">
              <source src="{pfx}media/research/rio-sio/system_demo_preview.mp4" type="video/mp4" />
              Your browser cannot play this video.
            </video>
          </div>
          <figcaption class="video-meta">
            <span class="video-meta-title">{c['demo']['video_title']}</span>
            <span class="video-meta-tag">{c['demo']['video_label']}</span>
          </figcaption>
        </figure>
      </div>
    </section>

    <!-- 01. The Challenge -->
    <section class="panel" id="story">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['challenge']['num']}</span>
          <h2>{c['challenge']['title']}</h2>
          <p class="lead">{c['challenge']['lead']}</p>
        </div>
        <div class="cols wide-left">
          <figure class="photo-card">
            <div class="photo-card-media standard-photo">
              <img alt="{c['challenge']['caption_2hi']}" loading="lazy" src="{pfx}media/research/rio-sio/2hi.jpg" />
            </div>
            <figcaption>{c['challenge']['caption_2hi']}</figcaption>
          </figure>
          <div class="story">
            <h3>{c['challenge']['story_title']}</h3>
            <p>{c['challenge']['story_p1']}</p>
            <p>{c['challenge']['story_p2']}</p>
            <div class="metricrow">
              <div class="metric">
                <strong>{c['challenge']['metric_cobot_val']}</strong>
                <span>{c['challenge']['metric_cobot_lbl']}</span>
              </div>
              <div class="metric">
                <strong>{c['challenge']['metric_cam_val']}</strong>
                <span>{c['challenge']['metric_cam_lbl']}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 02. System Design -->
    <section class="panel" id="optics">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['design']['num']}</span>
          <h2>{c['design']['title']}</h2>
          <p>{c['design']['lead']}</p>
        </div>
        <div class="cols">
          <figure class="photo-card">
            <div class="photo-card-media contain-technical" data-lightbox>
              <img alt="{c['design']['caption_concept']}" loading="lazy" src="{pfx}media/research/rio-sio/system_concept.jpg" data-zoomable />
            </div>
            <figcaption>{c['design']['caption_concept']} <span class="zoom-hint">🔍 Zoom</span></figcaption>
          </figure>
          <figure class="photo-card">
            <div class="photo-card-media standard-photo">
              <img alt="{c['design']['caption_sundial']}" loading="lazy" src="{pfx}media/research/rio-sio/5sunimpl.jpg" />
            </div>
            <figcaption>{c['design']['caption_sundial']}</figcaption>
          </figure>
        </div>
        <div class="metricrow" style="margin-top: 1.75rem;">
          <div class="metric">
            <strong>{c['design']['metric_directions_val']}</strong>
            <span>{c['design']['metric_directions_lbl']}</span>
          </div>
          <div class="metric">
            <strong>{c['design']['metric_led_val']}</strong>
            <span>{c['design']['metric_led_lbl']}</span>
          </div>
          <div class="metric">
            <strong>{c['design']['metric_uv_val']}</strong>
            <span>{c['design']['metric_uv_lbl']}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 03. Optical Design & Calibration -->
    <section class="panel" id="calibration">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['optics']['num']}</span>
          <h2>{c['optics']['title']}</h2>
          <p>{c['optics']['lead']}</p>
        </div>
        <div class="cols">
          <figure class="photo-card">
            <div class="photo-card-media contain-technical" data-lightbox>
              <img alt="{c['optics']['caption_6poc']}" loading="lazy" src="{pfx}media/research/rio-sio/6poc.jpg" data-zoomable />
            </div>
            <figcaption>{c['optics']['caption_6poc']} <span class="zoom-hint">🔍 Zoom</span></figcaption>
          </figure>
          <figure class="photo-card">
            <div class="photo-card-media contain-technical" data-lightbox>
              <img alt="{c['optics']['caption_6full']}" loading="lazy" src="{pfx}media/research/rio-sio/6full.jpg" data-zoomable />
            </div>
            <figcaption>{c['optics']['caption_6full']} <span class="zoom-hint">🔍 Zoom</span></figcaption>
          </figure>
        </div>
        <div style="height: 1.5rem;"></div>
        <div class="cols wide-left">
          <figure class="photo-card">
            <div class="photo-card-media standard-photo">
              <img alt="{c['optics']['caption_lab']}" loading="lazy" src="{pfx}media/research/rio-sio/20240603_170901.jpg" />
            </div>
            <figcaption>{c['optics']['caption_lab']}</figcaption>
          </figure>
          <figure class="photo-card">
            <div class="photo-card-media contain-technical" data-lightbox>
              <img alt="{c['optics']['caption_mirror']}" loading="lazy" src="{pfx}media/research/rio-sio/mirror0_375wave1706.jpg" data-zoomable />
            </div>
            <figcaption>{c['optics']['caption_mirror']} <span class="zoom-hint">🔍 Zoom</span></figcaption>
          </figure>
        </div>
        <p class="note" style="margin-top: 1.25rem; color: var(--text-muted); font-size: 0.85rem; font-family: var(--font-mono);">{c['optics']['note']}</p>
      </div>
    </section>

    <!-- 04. Multi-Angle Illumination -->
    <section class="panel" id="illumination">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['illumination']['num']}</span>
          <h2>{c['illumination']['title']}</h2>
          <p>{c['illumination']['lead']}</p>
        </div>
        
        <!-- Orderly 3-Column Macro Grid -->
        <div class="macro-grid">
          <figure class="macro-card">
            <div class="macro-img-wrap" data-lightbox>
              <img alt="{c['illumination']['caption_dig']}" loading="lazy" src="{pfx}media/research/rio-sio/8trdig.jpg" data-zoomable />
            </div>
            <figcaption>{c['illumination']['caption_dig']} <span class="zoom-hint">🔍 Zoom</span></figcaption>
          </figure>
          
          <figure class="macro-card">
            <div class="macro-img-wrap" data-lightbox>
              <img alt="{c['illumination']['caption_gp']}" loading="lazy" src="{pfx}media/research/rio-sio/8trgp.jpg" data-zoomable />
            </div>
            <figcaption>{c['illumination']['caption_gp']} <span class="zoom-hint">🔍 Zoom</span></figcaption>
          </figure>
          
          <figure class="macro-card">
            <div class="macro-img-wrap" data-lightbox>
              <img alt="{c['illumination']['caption_scratch']}" loading="lazy" src="{pfx}media/research/rio-sio/8trscratch.jpg" data-zoomable />
            </div>
            <figcaption>{c['illumination']['caption_scratch']} <span class="zoom-hint">🔍 Zoom</span></figcaption>
          </figure>
        </div>

        <div class="callout" style="margin-top: 1.5rem; border-left: 4px solid var(--accent-steel);">
          <h3>{c['illumination']['callout_title']}</h3>
          <p>{c['illumination']['callout_p']}</p>
          <p class="note" style="margin-top: 0.75rem; color: var(--text-muted); font-size: 0.82rem;">{c['illumination']['callout_note']}</p>
        </div>
      </div>
    </section>

    <!-- 05. Mechanical Engineering & Integration -->
    <section class="panel" id="mechanical">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['mechanical']['num']}</span>
          <h2>{c['mechanical']['title']}</h2>
          <p>{c['mechanical']['lead']}</p>
        </div>
        <div class="cols">
          <figure class="photo-card">
            <div class="photo-card-media standard-photo">
              <img alt="{c['mechanical']['caption_cad']}" loading="lazy" src="{pfx}media/research/rio-sio/9enclosure.jpg" />
            </div>
            <figcaption>{c['mechanical']['caption_cad']}</figcaption>
          </figure>
          <figure class="photo-card">
            <div class="photo-card-media standard-photo">
              <img alt="{c['mechanical']['caption_enclosure']}" loading="lazy" src="{pfx}media/research/rio-sio/20250914_174152.jpg" />
            </div>
            <figcaption>{c['mechanical']['caption_enclosure']}</figcaption>
          </figure>
        </div>
        <div style="height: 1.5rem;"></div>
        <div class="cols wide-left">
          <figure class="photo-card">
            <div class="photo-card-media standard-photo">
              <img alt="{c['mechanical']['caption_cabinet']}" loading="lazy" src="{pfx}media/research/rio-sio/5cabinet.jpg" />
            </div>
            <figcaption>{c['mechanical']['caption_cabinet']}</figcaption>
          </figure>
          <div class="callout">
            <h3>{c['mechanical']['callout_title']}</h3>
            <p>{c['mechanical']['callout_p']}</p>
            <p class="note" style="margin-top: 0.75rem; color: var(--text-muted); font-size: 0.82rem;">{c['mechanical']['callout_note']}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 06. Robot Handling & Calibration -->
    <section class="panel" id="robot">
      <div class="container">
        <div class="sectionhead" style="text-align: center; max-width: 820px; margin: 0 auto 1.5rem;">
          <span class="num">{c['robot']['num']}</span>
          <h2>{c['robot']['title']}</h2>
          <p style="margin: 0.5rem auto 0;">{c['robot']['lead']}</p>
        </div>
        <figure class="video-showcase" id="video2">
          <div class="video-frame">
            <video class="autoplay-when-visible" controls loop muted playsinline preload="metadata" poster="{pfx}media/research/rio-sio/robot_calibration_poster.jpg" aria-label="{c['robot']['video_title']}">
              <source src="{pfx}media/research/rio-sio/robot_calibration_preview.mp4" type="video/mp4" />
              Your browser cannot play this video.
            </video>
          </div>
          <figcaption class="video-meta">
            <span class="video-meta-title">{c['robot']['video_title']}</span>
            <span class="video-meta-tag">{c['robot']['video_label']}</span>
          </figcaption>
        </figure>
        <div class="callout" style="max-width: 880px; margin: 1.5rem auto 0; border-left: 4px solid var(--accent-steel);">
          <p style="font-size: 0.95rem; line-height: 1.65; margin: 0;">{c['robot']['after_video']}</p>
        </div>
      </div>
    </section>

    <!-- 07. Prototype in Action -->
    <section class="panel" id="results">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['results']['num']}</span>
          <h2>{c['results']['title']}</h2>
          <p>{c['results']['lead']}</p>
        </div>
        <div class="story">
          <h3>{c['results']['story_title']}</h3>
          <p>{c['results']['story_p1']}</p>
          <p>{c['results']['story_p2']}</p>
          <div class="metricrow">
            <div class="metric">
              <strong>{c['results']['metric_usaf_val']}</strong>
              <span>{c['results']['metric_usaf_lbl']}</span>
            </div>
            <div class="metric">
              <strong>{c['results']['metric_res_val']}</strong>
              <span>{c['results']['metric_res_lbl']}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 08. My Contribution -->
    <section class="panel" id="contribution">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['contribution']['num']}</span>
          <h2>{c['contribution']['title']}</h2>
          <p>{c['contribution']['lead']}</p>
        </div>
        <div class="cols">
          <div class="callout" style="border-left: 4px solid var(--accent-steel);">
            <h3>{c['contribution']['work_title']}</h3>
            <ul class="clean-list">
              {"".join([f"<li>{item}</li>" for item in c['contribution']['work_items']])}
            </ul>
          </div>
          <div class="callout">
            <h3>{c['contribution']['collab_title']}</h3>
            <p>{c['contribution']['collab_p1']}</p>
            <p>{c['contribution']['collab_p2']}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 09. Research Dissemination -->
    <section class="panel" id="publication">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['publication']['num']}</span>
          <h2>{c['publication']['title']}</h2>
          <p>{c['publication']['lead']}</p>
        </div>
        <div class="cols wide-left">
          <figure class="photo-card">
            <div class="photo-card-media standard-photo">
              <img alt="{c['publication']['caption_poster']}" loading="lazy" src="{pfx}media/research/rio-sio/20250506_172924.jpg" />
            </div>
            <figcaption>{c['publication']['caption_poster']}</figcaption>
          </figure>
          <div class="callout" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span class="kicker">{c['publication']['kicker']}</span>
              <h3 style="margin-top: 0.5rem;">{c['publication']['paper_title']}</h3>
              <p style="margin-top: 0.5rem; line-height: 1.6;">{c['publication']['paper_sub']}</p>
            </div>
            <div>
              <div style="margin-top: 1.25rem;">
                <a class="btn btn-primary btn-sm" href="https://doi.org/10.1117/12.3111698" rel="noopener noreferrer" target="_blank">{c['publication']['cta_paper']}</a>
              </div>
              <p class="note" style="margin-top: 0.75rem; color: var(--text-muted); font-size: 0.82rem;">{c['publication']['paper_note']}</p>
            </div>
          </div>
        </div>
        
        <div class="paper-explainer" style="margin-top: 3.5rem;">
          <div class="sectionhead" style="text-align: center; max-width: 820px; margin: 0 auto 1.5rem;">
            <span class="num">{c['publication']['explainer_num']}</span>
            <h3>{c['publication']['explainer_title']}</h3>
            <p style="margin: 0.5rem auto 0;">{c['publication']['explainer_sub']}</p>
          </div>
          <figure class="video-showcase" id="micro-video">
            <div class="video-frame">
              <video class="autoplay-when-visible" controls muted playsinline preload="metadata" poster="{pfx}media/research/rio-sio/micro_detective_poster.jpg" aria-label="{c['publication']['video_title']}">
                <source src="{pfx}media/research/rio-sio/The_Micro-Detective.mp4" type="video/mp4" />
                Your browser cannot play this video.
              </video>
            </div>
            <figcaption class="video-meta">
              <span class="video-meta-title">{c['publication']['video_title']}</span>
              <span class="video-meta-tag">{c['publication']['video_label']}</span>
            </figcaption>
          </figure>
          <div class="supporting-copy" style="max-width: 880px; margin: 1rem auto 0; text-align: center;">
            <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.6;">{c['publication']['explainer_copy']}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. Technical Documentation -->
    <section class="panel" id="documents">
      <div class="container">
        <div class="sectionhead">
          <span class="num">{c['documentation']['num']}</span>
          <h2>{c['documentation']['title']}</h2>
          <p>{c['documentation']['lead']}</p>
        </div>
        <div class="cols">
          <div class="pdfcard">
            <div class="ico">▣</div>
            <div>
              <strong>{c['documentation']['thesis_title']}</strong>
              <span>{c['documentation']['thesis_sub']}</span>
              <div style="margin-top: 0.85rem;">
                <span class="btn btn-outline btn-sm btn-disabled" style="cursor: not-allowed; opacity: 0.8;">
                  {c['documentation']['thesis_cta']}
                </span>
                <p class="note" style="margin-top: 0.5rem; color: var(--text-muted); font-size: 0.82rem;">{c['documentation']['thesis_note']}</p>
              </div>
            </div>
          </div>
          <div class="pdfcard">
            <div class="ico">↗</div>
            <div>
              <strong>{c['documentation']['paper_title']}</strong>
              <span>{c['documentation']['paper_sub']}</span>
              <div style="margin-top: 0.85rem;">
                <a href="https://doi.org/10.1117/12.3111698" rel="noopener noreferrer" target="_blank" class="btn btn-secondary btn-sm">
                  {c['documentation']['paper_cta']}
                </a>
              </div>
            </div>
          </div>
        </div>
        <div style="height: 1.75rem;"></div>
        <div class="callout" style="border-left: 4px solid var(--accent-steel);">
          <strong style="font-size: 1.05rem; display: block; color: var(--text-primary);">{c['documentation']['author_title']}</strong>
          <p style="margin-top: 0.5rem;">{c['documentation']['author_p']}</p>
        </div>
      </div>
    </section>
    """

    return render_html_shell(
        title=f"{p_title} | {site['site_name']}",
        description=p_oneliner,
        lang=lang,
        content=content,
        site=site,
        trans=trans,
        current_page=f"project-{project['id']}",
        depth=3
    )

def generate_project_detail(site, trans, project, lang):
    """Generates an individual project case study page."""
    if project["id"] == "rio-sio":
        return generate_rio_sio_detail(site, trans, project, lang)

    pfx = get_base_prefix(3)
    p_content = project["content"][lang]
    p_tmpl = trans["project_template"]
    p_id = project["id"]
    p_title = project["title"][lang]
    p_oneliner = project["one_liner"][lang]
    p_status = project["status"][lang]
    
    # Render specifications rows
    specs_rows = []
    for spec in p_content["specs"]:
        specs_rows.append(f"""
        <tr>
          <td class="spec-key">{spec['key']}</td>
          <td class="spec-val">{spec['value']}</td>
        </tr>
        """)
    specs_table_html = "".join(specs_rows)

    # Render contributions
    contrib_items = "".join([f"<li>{c}</li>" for c in p_content.get("contributions", [])])

    # Render external links
    links_html = []
    for link in project.get("links", []):
        if link.get("verified"):
            links_html.append(f"""
            <a href="{link['url']}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="width:100%; justify-content:flex-start; margin-bottom:0.5rem;">
              📄 {link['label']} ↗
            </a>
            """)
        else:
            links_html.append(f"""
            <div class="btn btn-outline btn-sm btn-disabled" style="width:100%; justify-content:flex-start; margin-bottom:0.5rem; text-align:left;">
              📄 {link['label']}<br>
              <span style="font-size:0.72rem; color:var(--text-muted); display:block;">{link.get('notice', '')}</span>
            </div>
            """)
    links_block = "".join(links_html) if links_html else f'<p style="font-size:0.85rem; color:var(--text-muted);">{"Documentation available upon request." if lang == "en" else "Dokumentation auf Anfrage erhältlich."}</p>'

    # Precision SVG Schematic with illustrative note
    detail_schematic_svg = render_schematic(p_id, lang, is_detail=True)
    schematic_caption_title = p_tmpl['schematic_caption_title']
    schematic_caption_sub = p_tmpl['schematic_caption_sub']

    content = f"""
    <!-- Project Detail Hero -->
    <section class="detail-hero">
      <div class="container">
        <a href="{pfx}{lang}/projects/" class="back-link">{p_tmpl['back_to_projects']}</a>

        <div class="detail-badge-group">
          <span class="hero-pill" style="margin-bottom:0;">{project['category_label'][lang]}</span>
          <span class="project-status-badge">{p_status}</span>
        </div>

        <h1 class="detail-title">{p_title}</h1>
        <p class="detail-one-liner">{p_oneliner}</p>

        <div class="detail-meta-bar">
          <div><strong>Status:</strong> {p_status}</div>
          <div><strong>{p_tmpl['timeline_label']}</strong> {project['period']}</div>
          <div><strong>{p_tmpl['organization_label']}</strong> {project['organization']}</div>
        </div>
      </div>
    </section>

    <!-- Detail Main Content -->
    <section class="container">
      <div class="detail-layout">
        <!-- Main Column -->
        <div class="detail-main">
          <!-- 1. Problem Statement -->
          <div>
            <h2 class="detail-section-title">
              <span style="color:var(--accent-steel);">01.</span> {p_tmpl['problem_label']}
            </h2>
            <p>{p_content['problem']}</p>
          </div>

          <!-- 2. Approach & Architecture -->
          <div>
            <h2 class="detail-section-title">
              <span style="color:var(--accent-steel);">02.</span> {p_tmpl['approach_label']}
            </h2>
            <p style="margin-bottom: 1.35rem;">{p_content['approach']}</p>

            <h4 style="font-size: 1rem; margin-bottom: 0.75rem; color: var(--text-primary);">{p_tmpl['contributions_title']}</h4>
            <ul class="contribution-list">
              {contrib_items}
            </ul>
          </div>

          <!-- 3. Engineering Problems & Iterations -->
          <div>
            <h2 class="detail-section-title">
              <span style="color:var(--accent-steel);">03.</span> {p_tmpl['iterations_label']}
            </h2>
            <p>{p_content['iterations']}</p>
          </div>

          <!-- 4. Results & Verification -->
          <div>
            <h2 class="detail-section-title">
              <span style="color:var(--accent-steel);">04.</span> {p_tmpl['results_label']}
            </h2>
            <p>{p_content['results']}</p>
          </div>

          <!-- 5. Lessons Learned -->
          <div>
            <h2 class="detail-section-title">
              <span style="color:var(--accent-steel);">05.</span> {p_tmpl['lessons_label']}
            </h2>
            <p>{p_content['lessons']}</p>
          </div>

          <!-- 6. Schematic / Architectural Gallery -->
          <div>
            <h2 class="detail-section-title">
              <span style="color:var(--accent-steel);">06.</span> {p_tmpl['gallery_label']}
            </h2>
            <div class="detail-schematic-container">
              {detail_schematic_svg}
              <div class="schematic-caption">
                <span>{schematic_caption_title}</span>
                <span>{schematic_caption_sub}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Sidebar Column -->
        <aside class="detail-sidebar">
          <!-- Specifications Table -->
          <div class="sidebar-box">
            <h3 class="sidebar-box-title">{p_tmpl['specs_label']}</h3>
            <table class="specs-table">
              <tbody>
                {specs_table_html}
              </tbody>
            </table>
          </div>

          <!-- Classification & Meta -->
          <div class="sidebar-box">
            <h3 class="sidebar-box-title">{p_tmpl['classification_title']}</h3>
            <div style="font-size: 0.88rem; color: var(--text-secondary); display: flex; flex-direction: column; gap: 0.5rem;">
              <div><strong>{p_tmpl['category_label']}</strong> {project['category_label'][lang]}</div>
              <div><strong>{p_tmpl['organization_label']}</strong> {project['organization']}</div>
              <div><strong>{p_tmpl['timeline_label']}</strong> {project['period']}</div>
            </div>
          </div>

          <!-- Publications & References -->
          <div class="sidebar-box">
            <h3 class="sidebar-box-title">{p_tmpl['publications_title']}</h3>
            {links_block}
          </div>

          <!-- Tags -->
          <div class="sidebar-box">
            <h3 class="sidebar-box-title">{p_tmpl['tags_title']}</h3>
            <div class="card-tags">
              {"".join([f'<span class="tag-pill">{t}</span>' for t in project['tags']])}
            </div>
          </div>
        </aside>
      </div>
    </section>
    """

    return render_html_shell(
        title=f"{p_title} | {site['site_name']}",
        description=p_oneliner,
        lang=lang,
        content=content,
        site=site,
        trans=trans,
        current_page=f"project-{p_id}",
        depth=3
    )

def generate_root_redirect():
    """Generates root index.html with language auto-detection."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=en/">
  <title>Kunal Bhai Patel — Engineer & Maker</title>
  <script>
    (function() {
      var saved = localStorage.getItem('kunal_portfolio_lang');
      var lang = saved || (navigator.language && navigator.language.toLowerCase().startsWith('de') ? 'de' : 'en');
      window.location.replace(lang + '/');
    })();
  </script>
</head>
<body style="background:#101418; color:#f3f4f2; font-family:sans-serif; text-align:center; padding:5rem 1rem;">
  <p>Redirecting to Kunal Bhai Patel portfolio... / Weiterleitung zum Portfolio...</p>
  <p><a href="en/" style="color:#7896ad;">English</a> · <a href="de/" style="color:#7896ad;">Deutsch</a></p>
</body>
</html>
"""

def generate_404(site):
    """Generates a clean 404.html page for GitHub Pages."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Not Found | {site['site_name']}</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body style="background: var(--bg-canvas); color: var(--text-primary); font-family: var(--font-sans); display: flex; align-items: center; justify-content: center; min-height: 100vh; text-align: center; padding: 2rem;">
  <div>
    <h1 style="font-size: 3rem; margin-bottom: 1rem; color: var(--accent-steel);">404</h1>
    <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem;">Page Not Found / Seite nicht gefunden</h2>
    <p style="max-width: 520px; margin-bottom: 2rem; color: var(--text-secondary);">
      The requested route does not exist. You may return to the English or German homepage below.<br><br>
      Die angeforderte Seite existiert nicht. Sie können zur englischen oder deutschen Startseite zurückkehren.
    </p>
    <div style="display: flex; justify-content: center; gap: 1rem;">
      <a href="en/" class="btn btn-primary">English Homepage</a>
      <a href="de/" class="btn btn-secondary">Deutsche Startseite</a>
    </div>
  </div>
</body>
</html>
"""

def build_site():
    print("=== Starting Kunal Bhai Patel Portfolio Static Build ===")
    
    # 1. Ensure dist exists
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Copy static assets (css, js, media)
    css_dist = DIST_DIR / "css"
    js_dist = DIST_DIR / "js"
    css_dist.mkdir(parents=True, exist_ok=True)
    js_dist.mkdir(parents=True, exist_ok=True)
    
    shutil.copy(SRC_DIR / "css" / "style.css", css_dist / "style.css")
    shutil.copy(SRC_DIR / "js" / "main.js", js_dist / "main.js")
    
    public_dir = BASE_DIR / "public"
    if public_dir.exists():
        for item in public_dir.iterdir():
            if item.is_dir():
                shutil.copytree(item, DIST_DIR / item.name, dirs_exist_ok=True)
            else:
                shutil.copy(item, DIST_DIR / item.name)
        print("✓ Copied public assets to dist/")
    print("✓ Copied CSS and JS to dist/")

    # 3. Load structured content
    site = load_json(CONTENT_DIR / "site.json")
    trans_en = load_json(CONTENT_DIR / "translations" / "en.json")
    trans_de = load_json(CONTENT_DIR / "translations" / "de.json")

    # Load all project definitions
    project_files = glob.glob(str(CONTENT_DIR / "projects" / "*.json"))
    projects = [load_json(f) for f in project_files]
    projects.sort(key=lambda p: (not p.get("featured", False), p["id"]))
    print(f"✓ Loaded {len(projects)} structured project files")

    # 4. Generate root index.html (redirector) and 404.html
    with open(DIST_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_root_redirect())
    with open(DIST_DIR / "404.html", "w", encoding="utf-8") as f:
        f.write(generate_404(site))
    print("✓ Generated root redirector index.html and 404.html")

    # 5. Generate dedicated pages for EN and DE
    en_dir = DIST_DIR / "en"
    de_dir = DIST_DIR / "de"
    en_dir.mkdir(parents=True, exist_ok=True)
    de_dir.mkdir(parents=True, exist_ok=True)

    # 5.1 Homepages (/en/, /de/)
    with open(en_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_homepage(site, trans_en, projects, "en"))
    with open(de_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_homepage(site, trans_de, projects, "de"))
    print("✓ Generated EN and DE Homepages (/en/, /de/)")

    # 5.2 Projects Pages (/en/projects/, /de/projects/)
    en_proj_dir = en_dir / "projects"
    de_proj_dir = de_dir / "projects"
    en_proj_dir.mkdir(parents=True, exist_ok=True)
    de_proj_dir.mkdir(parents=True, exist_ok=True)

    with open(en_proj_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_projects_page(site, trans_en, projects, "en"))
    with open(de_proj_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_projects_page(site, trans_de, projects, "de"))
    print("✓ Generated EN and DE Projects Pages (/en/projects/, /de/projects/)")

    # 5.3 Research Pages (/en/research/, /de/research/)
    en_res_dir = en_dir / "research"
    de_res_dir = de_dir / "research"
    en_res_dir.mkdir(parents=True, exist_ok=True)
    de_res_dir.mkdir(parents=True, exist_ok=True)

    with open(en_res_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_research_page(site, trans_en, "en"))
    with open(de_res_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_research_page(site, trans_de, "de"))
    print("✓ Generated EN and DE Research Pages (/en/research/, /de/research/)")

    # 5.4 About Pages (/en/about/, /de/about/)
    en_abt_dir = en_dir / "about"
    de_abt_dir = de_dir / "about"
    en_abt_dir.mkdir(parents=True, exist_ok=True)
    de_abt_dir.mkdir(parents=True, exist_ok=True)

    with open(en_abt_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_about_page(site, trans_en, "en"))
    with open(de_abt_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_about_page(site, trans_de, "de"))
    print("✓ Generated EN and DE About Pages (/en/about/, /de/about/)")

    # 5.5 Contact Pages (/en/contact/, /de/contact/)
    en_con_dir = en_dir / "contact"
    de_con_dir = de_dir / "contact"
    en_con_dir.mkdir(parents=True, exist_ok=True)
    de_con_dir.mkdir(parents=True, exist_ok=True)

    with open(en_con_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_contact_page(site, trans_en, "en"))
    with open(de_con_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_contact_page(site, trans_de, "de"))
    print("✓ Generated EN and DE Contact Pages (/en/contact/, /de/contact/)")

    # 6. Generate project detail pages for all 6 projects
    for proj in projects:
        p_id = proj["id"]
        # Generate for en
        p_en_dir = en_proj_dir / p_id
        p_en_dir.mkdir(parents=True, exist_ok=True)
        with open(p_en_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(generate_project_detail(site, trans_en, proj, "en"))

        # Generate for de
        p_de_dir = de_proj_dir / p_id
        p_de_dir.mkdir(parents=True, exist_ok=True)
        with open(p_de_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(generate_project_detail(site, trans_de, proj, "de"))
            
    print(f"✓ Generated bilingual project detail pages for {len(projects)} projects (including Rio sio, Plottu, HDD enclosure, Home server, 3D printing, Local AI)")

    # 7. Add .nojekyll for GitHub Pages
    with open(DIST_DIR / ".nojekyll", "w", encoding="utf-8") as f:
        f.write("")
    print("✓ Created .nojekyll for GitHub Pages")

    print("\n=== Static Build Succeeded! Output directory: dist/ ===")

if __name__ == "__main__":
    build_site()
