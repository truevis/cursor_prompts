# Write README.md from the codebase

Write a clear `README.md` for this project based on the code and materials in the workspace.

## Include

- **What it is** — one short paragraph on purpose and audience
- **Features** — concise bullet list of what users can do
- **Project layout** — important files/folders and what they own
- **How it works** — explain main logic/flow (entry point → data → UI), not line-by-line narration
- **Configuration** — env vars, secrets, `.streamlit/config.toml`, model keys, etc., without inventing values (names/purpose only; no setup steps)

## Streamlit apps

If this is a Streamlit app, also document:

- Entry file (`app.py`, `streamlit_app.py`, or equivalent)
- Pages / navigation structure
- Any theme or Cloud-specific notes that are already in the repo

## Exclude

- **All installation info** — no install, setup, `pip`/`uv`/`npm`, virtualenv, cloning, or “getting started” environment steps
- **How to run** — no `streamlit run`, local server, or deploy-from-scratch tutorials
- **Dependencies as install guidance** — do not add a Dependencies/Install section; naming major libraries only belongs inside Features or How it works if useful for understanding, not for installing
- Marketing fluff, badges spam, or unverified claims
- Secrets, API keys, or internal credentials

## Optional screenshot

- Path: `img/screenshot.png`

## Style

- Accurate to the code; do not invent features
- Prefer short sections and scannable bullets
- Use the project's existing tone if a README already exists

