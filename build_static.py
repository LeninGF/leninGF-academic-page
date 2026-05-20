"""Prerender Flask templates into static HTML for GitHub Pages.

Usage:
    python build_static.py

Output goes to ./_site/ — a self-contained static copy of the site.
The Flask app (app.py) is NOT modified.
"""

import sys
import os
import shutil

# Allow importing app from parent directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import render_template
from app import app as _app, PROFILE, PUBLICATIONS, RESEARCH_INTERESTS, EDUCATION, EXPERIENCE

# Configure server name so url_for works outside an active request
_app.config["SERVER_NAME"] = "localhost:5000"
_app.config["APPLICATION_ROOT"] = "/"
_app.config["PREFERRED_URL_SCHEME"] = "http"

SITE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_site")
STATIC_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

ROUTES = {
    "index":        {"template": "index.html",        "path": "index.html",        "active": "home"},
    "publications": {"template": "publications.html", "path": "publications.html", "active": "publications"},
    "research":     {"template": "research.html",     "path": "research.html",     "active": "research"},
    "cv":           {"template": "cv.html",            "path": "cv.html",          "active": "cv"},
}

def build():
    # Clean and recreate _site
    if os.path.exists(SITE_DIR):
        shutil.rmtree(SITE_DIR)
    os.makedirs(SITE_DIR)

    # Copy static files
    shutil.copytree(STATIC_SRC, os.path.join(SITE_DIR, "static"))

    # Render each page
    with _app.app_context():
        for name, info in ROUTES.items():
            html = render_template(
                info["template"],
                profile=PROFILE,
                publications=PUBLICATIONS,
                interests=RESEARCH_INTERESTS,
                education=EDUCATION,
                experience=EXPERIENCE,
                active=info["active"],
            )
            out_path = os.path.join(SITE_DIR, info["path"])
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  ✓ {info['path']}")

    print(f"\nStatic site generated in ./_site/ ({len(ROUTES)} pages)")


if __name__ == "__main__":
    build()
