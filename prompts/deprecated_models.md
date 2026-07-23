# Deprecated model migration

Find and replace deprecated AI model IDs across the repo. Verify current deprecation guidance with official sources before finalizing. Preserve provider prefixes and ID formats.

## Agent prompt

```text
Update deprecated model references across this repository.

Objectives:
1) Find deprecated model IDs in active code, config, tests, and docs.
2) Replace them with approved target model IDs (confirm via official docs/web).
3) Preserve provider-specific prefixes and ID formats.
4) Keep replacements consistent in assignments, literals, and user-facing labels.
5) Leave zero deprecated IDs in active runtime paths.
6) Cite the official pages used for verification.

Execution order:
1) Web-check official deprecation/replacement guidance.
2) Update runtime paths first (app entry, config, API wrappers, Streamlit model selectboxes).
3) Update tests and automation.
4) Update docs/examples.
5) Optionally update commented-out code.

Verification:
- Search confirms old IDs are gone from active code.
- New IDs appear where expected.
- Report files changed, old→new mapping, and verification links.
- Light syntax/lint check on touched files.
```

## Default Gemini mappings (verify before use)

These are project defaults—re-validate against live docs; naming changes often.

### OpenRouter (`google/` prefix)

| Old | New |
|-----|-----|
| `google/gemini-2.5-pro` | `google/gemini-3.1-pro-preview` |
| `google/gemini-2.5-flash` | `google/gemini-3-flash-preview` |
| `google/gemini-2.5-flash-preview-09-2025` | `google/gemini-3-flash-preview` |
| `google/gemini-2.5-flash-lite-preview-09-2025` | `google/gemini-3-flash-preview` |
| `google/gemini-3-pro-preview` | `google/gemini-3.1-pro-preview` |

### Direct Gemini API (`models/` prefix)

Normalize selections to:

- `models/gemini-flash-latest`
- `models/gemini-flash-lite-latest`
- `models/gemini-pro-latest`

Keep `google/` vs `models/` prefixes exact.

## Where to look (Streamlit apps)

1. Model defaults and `st.selectbox` / radio options (`app.py`, `config.py`, `settings.py`)
2. Provider clients and routers (`utils/`, API wrappers)
3. Tests and QA scripts
4. README / help copy that names models

## Search patterns

```bash
rg "gemini|google/gemini|models/gemini"
rg "gemini-2\\."
rg "google/gemini-2\\.5-(pro|flash)"
rg "MODEL|default_model|model_mapping|Choose AI Model"
```

## Checklist

- [ ] Official sources checked this run
- [ ] Runtime updated first
- [ ] Tests/docs updated
- [ ] Prefixes preserved
- [ ] No deprecated IDs in active code
- [ ] Streamlit model pickers show current IDs/labels

## Sources to re-check

- https://ai.google.dev/gemini-api/docs/deprecations
- https://openrouter.ai/announcements
