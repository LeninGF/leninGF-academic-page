# Session Journal — Personal Academic Web Page

**Date:** 2026-05-20
**Model:** DeepSeek V4 Flash (via DeepCode)
**Task:** Create a basic personal academic web page using Flask

---

## Request

> "Create a basic personal academic web page using flask. Find information about myself, My name is Lenin Gonzalo Falconi Estrada. I have a github LeninGF, I work at Escuela Politecnica Nacional. I am a PhD student. I have attended several proceedings and published some stuff. List my works. My research is related to medical imaging and deep learning. Currently focusing on Image Segmentation for Thermogram and Mammogram Images in Breast Cancer."

## Key Decisions

### 1. Information Source
- Used the web search tool to find the user's ORCID (0000-0003-4402-6643).
- The ORCID public API was queried to retrieve bio, education, and publications.
- Bio was fetched from `pub.orcid.org/v3.0/0000-0003-4402-6643/person`.
- Publications were fetched from `pub.orcid.org/v3.0/0000-0003-4402-6643/works`.

### 2. Publications (from ORCID)
All three publications focus on transfer learning for mammogram classification:
- **2019** — IWSSIP Conference: MobileNet and NASNet for breast mammogram abnormalities
- **2020** — CBMS Conference: BI-RADS classification via transfer learning and fine tuning
- **2020** — ASTESJ Journal: Mammogram abnormalities classification on CBIS-DDSM

### 3. Stack
- **Flask** (Python web framework)
- **Jinja2 templates** (server-side rendering)
- **No CSS framework** — pure custom CSS
- **No JavaScript dependencies** — vanilla JS for theme toggle only

### 4. Page Structure
- **Sidebar layout** (fixed left sidebar, scrollable main content)
- Pages: Home, Research, Publications, CV
- Sidebar contains: avatar, name, affiliation, social links, navigation, theme toggle
- Social links added: Email, ORCID, GitHub, Google Scholar, LinkedIn, ResearchGate

### 5. Social Links Added
| Platform | URL | Source |
|---|---|---|
| Email | lenin.falconi@epn.edu.ec | ORCID bio |
| ORCID | https://orcid.org/0000-0003-4402-6643 | User-provided |
| GitHub | https://github.com/LeninGF | User-provided |
| LinkedIn | https://www.linkedin.com/in/lenin-g-falconi | Web search + user confirmation |
| ResearchGate | https://www.researchgate.net/profile/Lenin-Falconi | Web search |
| Google Scholar | https://scholar.google.com/citations?user=4Xk02pkAAAAJ&hl=en&oi=ao | User-provided |

### 6. Bug Fix
- Publications and Research pages showed no content because `profile` was not passed to their templates. The footer also referenced `profile.year` which didn't exist.
- **Fix:** All routes now pass all data objects (`profile`, `publications`, `interests`, `education`, `experience`) to every template.

### 7. Theme Toggle (Dark/Light Mode)
- Added a button at the bottom of the sidebar.
- Uses CSS custom properties (`body.dark` overrides `:root` variables).
- Persists preference via `localStorage`.
- Respects system `prefers-color-scheme: dark` on first visit.

### 8. Folder Name
- Originally created as `hello-world-deepcode` (generic test name).
- Renamed to `leninGF-academic-page` at the user's request.

### 9. Filename
The journal file was named `session-journal.md` at the user's initiative. The user noted this pattern should be remembered for future tasks.

---

## Files Created/Modified

| File | Action |
|---|---|
| `app.py` | Created — Flask app with data and routes |
| `requirements.txt` | Created — Flask dependency |
| `static/style.css` | Created — Full styling + dark theme |
| `templates/base.html` | Created — Layout, sidebar, theme toggle, JS |
| `templates/index.html` | Created — Home page with bio and quick links |
| `templates/research.html` | Created — Research interests cards |
| `templates/publications.html` | Created — Journal + conference publication lists |
| `templates/cv.html` | Created — Education and experience timeline |
| `session-journal.md` | Created — This file |

---

## Session 2 — 2026-05-20: Git Setup, Static Build, and Deployment Planning

### 10. Git Initialization & First Commit
- Repository initialized with `git init`.
- `.gitignore` added for `__pycache__/`.
- Initial commit `d320d09` with message `leninGF-academic-page`.
- Remote added (`https://github.com/LeninGF/leninGF-academic-page.git`) and pushed to `master`.

### 11. GitHub Pages Feasibility
- Flask is a server-side Python app — **cannot run directly** on GitHub Pages (static only).
- Two deployment options identified:
  - **Render.com** — runs the full Flask app (free tier, URL: `https://lenin-gf-academic-page.onrender.com`)
  - **GitHub Pages** — pre-rendered static snapshot (URL: `https://leningf.github.io/leninGF-academic-page/`)

### 12. Static Build Script (`build_static.py`)
- Created a build script that pre-renders all Flask Jinja2 templates into plain HTML using `app.test_request_context()`.
- Output goes to `_site/` directory (added to `.gitignore` so the Flask repo stays clean).
- The Flask app (`app.py`) remains unchanged — both deployment methods coexist.
- Run with: `python build_static.py`

### 13. Files Added
| File | Action |
|---|---|
| `README.md` | Created — project description and local dev instructions |
| `TODO.org` | Created — Emacs org file with pending deployment tasks |
| `build_static.py` | Created — pre-renders Flask templates to `_site/` |
| `requirements.txt` | Modified — added `gunicorn==23.0.0` for Render |

### 14. Branch Rename: `master` → `main`
- Local branch renamed from `master` to `main` (`git branch -m master main`).
- Pushed `main` to GitHub (`origin/main`).
- GitHub default branch still points to `master` — must be changed manually in **Settings → Branches** on GitHub.

### Files (as of commit `8292341`)

```
.gitignore
README.md
TODO.org
app.py
build_static.py
requirements.txt
session-journal.md
static/style.css
templates/base.html
templates/cv.html
templates/index.html
templates/publications.html
templates/research.html
```

## How to Run (Flask)

```bash
cd /home/leningfe/PythonProjects/agentic-ai-tests/leninGF-academic-page
pip install -r requirements.txt
python app.py
# Opens at http://localhost:5000
```

## How to Build Static Site

```bash
python build_static.py
# Output: ./_site/ (4 HTML pages + static/)
```
