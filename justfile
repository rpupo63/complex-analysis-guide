# Build the guide and run all checks (run this before publishing).
check: build
    .venv/bin/python check.py

build:
    python3 build.py
    node tools/prerender.mjs

# Compare the build with the frozen v17 reference (the migration gate).
roundtrip: build
    python3 tools/roundtrip.py

# One-time setup for the render checks.
setup:
    python3 -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    npm install
