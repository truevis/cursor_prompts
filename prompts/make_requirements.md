# Create `requirements.txt` for Streamlit Community Cloud

Create or update `requirements.txt` for this Streamlit app so it deploys cleanly on Streamlit Community Cloud.

## Rules

1. Include only third-party packages the app actually imports/needs at runtime.
2. Pin each package to a recent stable version with `==` (e.g. `pandas==2.2.3`).
3. One package per line; filename exactly `requirements.txt` (lowercase).
4. Do **not** list stdlib modules.
5. Prefer omitting `streamlit` (Cloud provides it). Add/pin `streamlit==...` only if the app needs a specific version feature or the project already pins it.
6. Match versions to what the code uses (e.g. if you use APIs from a major release, pin that major).
7. Do not add dev-only tools (pytest, black, ruff) unless this file is explicitly for a full env and the user asks.
8. After editing, sanity-check that every non-stdlib import in the app entrypoints has a requirement (or is provided by Cloud).

## Format

```text
package-name==X.Y.Z
another-package==X.Y.Z
```

## Deliver

- Write `requirements.txt`
- Briefly list packages added/removed and why
