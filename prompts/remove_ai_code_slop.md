---
name: deslop
description: Remove AI-generated code slop and clean up code style while preserving behavior
---

# Remove AI code slop

Review the relevant code and remove AI-generated slop. Match local style. Keep behavior the same unless fixing a clear bug.

## Focus areas

- Comments that restate the obvious or clash with surrounding style
- Defensive `try/except` or null-checks on trusted paths that the codebase does not use elsewhere
- Deep nesting that should be early returns
- Dead code, unused imports, and “just in case” parameters
- Over-abstracted helpers used once
- Inconsistent naming or patterns vs neighboring files

## Streamlit-specific slop

- Large custom CSS when `.streamlit/config.toml` / native widgets would do
- Redundant `st.rerun()` / session-state writes that fight Streamlit’s model
- Emoji decoration and filler markdown with no UX value
- Duplicate `st.set_page_config` or config called after other Streamlit commands
- Wrapper functions that only call a single Streamlit API once
- Inflated spinner/status theater around instant operations

## Guardrails

- Prefer minimal, focused edits over rewrites
- Do not change product behavior for style alone
- Do not “modernize” APIs unless needed for the cleanup or already used nearby
- Final summary: 1–3 sentences on what was removed and why
