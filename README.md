# Kunal Bhai Patel — Personal Engineering & Maker Portfolio

This repository contains the source code, content architecture, and static build system for Kunal Bhai Patel's personal bilingual engineering and maker portfolio website.

The portfolio is designed as a **balanced showcase** presenting professional mechatronics/optical inspection research and independent hands-on maker projects with equal 50/50 visual and structural prominence.

---

## ⚡ 1-Click Windows Launcher

On Windows, simply double-click:
```bat
START_WEBSITE.bat
```
This script automatically:
1. Validates Python 3 on your system.
2. Rebuilds the entire static site from source data into `dist/`.
3. Opens your default web browser to [http://localhost:8080/en/](http://localhost:8080/en/).
4. Starts the local preview server on port 8080.

---

## 🛠 Architectural Overview

The portfolio uses a **zero-dependency static site generator** implemented in standard Python 3. It generates pre-rendered, 100% static HTML, modern CSS with CSS custom properties, and lightweight vanilla JS. No external npm, node, or heavy frontend frameworks are required.

```
Portfolio/
├── START_WEBSITE.bat            # 1-Click Windows launcher (builds, opens browser & serves)
├── content/                     # Source-of-truth structured data
│   ├── site.json                # Global metadata, credentials, links, author profile
│   ├── translations/
│   │   ├── en.json              # English copy, labels, accessibility strings
│   │   └── de.json              # German copy, labels, accessibility strings
│   └── projects/                # Modular project catalog (6 JSON definitions)
│       ├── rio-sio.json         # P01: Robotic Inspection of Optical Surfaces (Professional/Research)
│       ├── plottu.json          # M01: Wi-Fi Desktop Pen Plotter (Personal/Maker)
│       ├── hdd-enclosure.json   # M02: Custom Dual-HDD Cooling Enclosure
│       ├── home-server.json     # M04: Debian 12 Home Server & Self-Hosting
│       ├── 3d-printing.json     # M03: 3D Printing & Mechanical Prototyping
│       └── local-ai.json        # M05: Local AI & Voice Assistant Experiments
├── src/
│   ├── css/
│   │   └── style.css            # Dual-theme design system (Dark & Editorial Light)
│   └── js/
│       └── main.js              # Theme switcher, drawer, filter tabs, language switcher
├── dist/                        # 100% pre-rendered static output for GitHub Pages
│   ├── index.html               # Root redirector (detects browser language / saved preference)
│   ├── 404.html                 # Bilingual 404 handler
│   ├── .nojekyll                # Disables Jekyll processing on GitHub Pages
│   ├── en/                      # English multi-page structure
│   │   ├── index.html           # /en/ (Home)
│   │   ├── projects/            # /en/projects/ (Projects gallery & case studies)
│   │   ├── research/            # /en/research/ (Metrology & SPIE paper)
│   │   ├── about/               # /en/about/ (Bio, training, & "About This Website")
│   │   └── contact/             # /en/contact/ (LinkedIn, inquiries, CV request)
│   ├── de/                      # German multi-page structure
│   │   ├── index.html           # /de/ (Startseite)
│   │   ├── projects/            # /de/projects/ (Projekte & Fallstudien)
│   │   ├── research/            # /de/research/ (Forschung & SPIE-Publikation)
│   │   ├── about/               # /de/about/ (Werdegang & „Über diese Website“)
│   │   └── contact/             # /de/contact/ (Kontakt & Austausch)
│   ├── css/                     # Production stylesheet
│   └── js/                      # Production scripts
├── docs/                        # Project specifications and source documentation
├── build.py                     # Deterministic build script (Python 3 standard library)
├── serve.py                     # Local preview server
└── README.md                    # This documentation
```

---

## 📄 Hybrid Multi-Page Routing

Each major section has an independent, dedicated static HTML page:

| Section | English URL | German URL | Depth |
| :--- | :--- | :--- | :--- |
| **Home / Startseite** | `/en/` | `/de/` | `../` |
| **Projects / Projekte** | `/en/projects/` | `/de/projects/` | `../../` |
| **Research / Forschung** | `/en/research/` | `/de/research/` | `../../` |
| **About / Über mich** | `/en/about/` | `/de/about/` | `../../` |
| **Contact / Kontakt** | `/en/contact/` | `/de/contact/` | `../../` |
| **Project Details (e.g. Rio sio)** | `/en/projects/rio-sio/` | `/de/projects/rio-sio/` | `../../../` |
| **Project Details (e.g. Plottu)** | `/en/projects/plottu/` | `/de/projects/plottu/` | `../../../` |

All navigation links and language switcher anchors use depth-aware relative paths (`pfx`), guaranteeing 100% portability whether hosted on `localhost:8080`, GitHub Pages root (`USERNAME.github.io`), or viewed offline.

---

## 🎨 Dual Theme Architecture: Dark & Editorial Light

- **Dark Theme (Default)**: Charcoal (`#101418`), Slate (`#171F26`), Steel Blue (`#7896AD`), and Off-White (`#F3F4F2`).
- **Editorial Light Theme**: Clean engineering off-white (`#F6F6F3`), pure white cards (`#FFFFFF`), deep charcoal slate text (`#17212B`), muted steel blue accents (`#607F96`), and hairline grey borders (`#E0E4E7`).
- **Instant Anti-FOUC**: A lightweight synchronous script in `<head>` queries `localStorage` and `prefers-color-scheme` before CSS renders, preventing any white or dark flashes on page load.
- **Header Theme Toggle**: Intuitive sun/moon toggle with full accessibility labels and state persistence.

---

## 🌐 Bilingual Support & Deep Link Symmetry

- **Path-Preserving Toggle**: Switching language from `/en/research/` immediately navigates to `/de/research/` (and vice-versa).
- **Authentic Engineering Terminology**: Natural technical German (e.g., *Kinematik, FDM-3D-Druck, Gewindeeinsätze, optische Oberflächenprüfung*) and precise English.
- **No Third-Party Widgets**: 100% pre-rendered and deterministic.

---

## 💻 Manual Commands

### 1. Build Static Files
```bash
python build.py
```

### 2. Run Local Preview Server
```bash
python serve.py 8080
```
Open [http://localhost:8080/](http://localhost:8080/) in your browser.
