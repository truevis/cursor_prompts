# Streamlit-oriented Cursor prompts

Prompts and lightweight rules for improving Streamlit apps (and related chores) in Cursor. Attach with `@prompts/filename.md` in chat/composer. Aimed at developers polishing Streamlit UX, deps, docs, and model usage without fighting the Agent.

## Features

- Baseline Streamlit edit rules (`AGENTS.md` / `cursorrules.md`) that preserve behavior and avoid unnecessary restarts
- Visual polish and theming prompts (theme-first, paperwhite `config.toml`)
- Responsive layout audit with Streamlit-specific failure modes
- Chat/LLM dollar-amount safety (`no_latex.md`) and local-module hot reload (`importlib-skill.md`)
- Community Cloud–oriented `requirements.txt` pinning and README write/refresh prompts
- Cleanup and workflow helpers: deslop, deprecated Gemini/OpenRouter model migration, RIPER-5 protocol

## Project layout

| Path | Owns |
|------|------|
| `AGENTS.md` | Cursor Agent rules for Streamlit work (also available as `cursorrules.md`) |
| `cursorrules.md` | Same rules as `AGENTS.md`; use with `@cursorrules.md` in Composer |
| `prompts/make_app_look_better.md` | Visual/UX polish with native Streamlit patterns |
| `prompts/paperwhite_theme.md` | Warm e-reader theme via `.streamlit/config.toml` |
| `prompts/responsive_check.md` | Desktop + mobile layout find/fix checklist |
| `prompts/no_latex.md` | Stop `$...$` LaTeX from breaking dollar amounts |
| `prompts/importlib-skill.md` | Hot-reload local modules during Streamlit development |
| `prompts/make_requirements.md` | Pinned `requirements.txt` for Community Cloud |
| `prompts/make_readme.md` | Write a README from the codebase |
| `prompts/update_readme.md` | Refresh README **without** install/run sections |
| `prompts/remove_ai_code_slop.md` | Strip AI-style noise; keep behavior |
| `prompts/deprecated_models.md` | Migrate deprecated Gemini/OpenRouter model IDs |
| `prompts/riper.md` | RESEARCH → INNOVATE → PLAN → EXECUTE → REVIEW protocol |
| `prompts/paste_html_to_md .py` | Small HTML→Markdown helper script |
| `scripts/upgrade*.bat` | Local pip upgrade helpers (optional utilities) |

## How it works

1. Open a Streamlit (or related) app repo in Cursor.
2. Attach one or more prompts with `@prompts/filename.md`.
3. Add app context (entrypoint, constraints, brand) when it matters.
4. Prefer pairing a task prompt with `@cursorrules.md` or `@AGENTS.md` for safer edits.

These prompts complement Cursor Agent Skills for Streamlit; they do not replace them. Prefer native Streamlit theming and layout over large CSS dumps.

## Configuration

No project-level env vars or secrets. Prompt-specific knobs live in the files themselves (for example, paperwhite palette / `config.toml` keys in `prompts/paperwhite_theme.md`, and Gemini model ID tables in `prompts/deprecated_models.md`). Re-verify model IDs against official docs before relying on them.

## Tips

- Be specific about entrypoint (`app.py` / `streamlit_app.py`) and must-keep behaviors.
- Theme and layout before CSS; CSS only for confirmed gaps.
- Keep `prompts/make_requirements.md` guidance aligned with runtime imports on deployable apps.

## Contributing

- Add focused prompts with clear constraints and a short “deliver” section.
- Prefer Streamlit-native guidance when the task is Streamlit-related.
- Keep filenames lowercase with underscores.

## License

MIT

## Authors

- Initial prompt collection — Eric Boehlke

## Acknowledgments

- [Streamlit prompt library discussion](https://discuss.streamlit.io/t/lets-make-a-prompt-library-for-cursor-streamlit/79937/3)
