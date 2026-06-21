# AGENTS.md

## Cursor Cloud specific instructions

This repository (`for-all-temps`) is a scratch/experiments repo. At the time of
setup it contained only `README.md` — there is no application, package manager
manifest (`package.json`, `requirements.txt`, etc.), test suite, or build step.

Intended work (per the repo owner's rules) is **vanilla browser experiments**
using only built-in web APIs (Canvas, WebAudio, etc.) with **no external
dependencies** (no npm packages, no CDN frameworks). Keep that constraint in mind
when adding code here.

### Runtimes available on the VM
- Node.js `v22` / npm `10` and Python `3.12` are preinstalled. No project-level
  install step is needed unless a manifest is later added.

### Running experiments (dev workflow)
Because experiments are static HTML/JS/CSS, serve the repo root with any static
server and open it in a browser, e.g.:

```bash
python3 -m http.server 8000   # then open http://localhost:8000/
```

There is no lint/test/build tooling configured. If a JS project is later added
(a `package.json` appears), the startup update script will run `npm install`
automatically; add lint/test/build notes here at that point.
