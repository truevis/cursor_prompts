# Paperwhite theme (Streamlit)

Create a paperwhite / e-reader inspired theme for this Streamlit app: warm paper backgrounds, high readability, calm contrast. Prefer `.streamlit/config.toml`. Use CSS only for gaps Streamlit theme keys cannot cover.

## Goals

- Comfortable long-form reading and data browsing
- Warm, minimal, elegant—not cold or clinical
- WCAG AA contrast for body text
- Preserve app behavior; theme only

## Palette

| Role | Value | Notes |
|------|-------|--------|
| Primary background | `#F5F1E8` | Warm paper |
| Secondary background | `#FAF8F3` | Widgets / elevated surfaces |
| Text | `#2C2416` | Warm dark brown (not pure black) |
| Secondary text feel | `#5C4E3D` | Captions, help (via theme gray / muted UI) |
| Primary / accent | `#8B7355` | Buttons, links, focus |
| Borders | `#E5DDD0` | Soft separation |
| White surfaces | `#FFFFFF` | Optional cards / code if needed |

Accent hover target when custom CSS is required: `#6B5B4F`.

## Streamlit theme (required)

Create or update `.streamlit/config.toml`:

```toml
[theme]
base = "light"
primaryColor = "#8B7355"
backgroundColor = "#F5F1E8"
secondaryBackgroundColor = "#FAF8F3"
textColor = "#2C2416"
linkColor = "#6B5B4F"
borderColor = "#E5DDD0"
font = "serif"

# Optional refinements if supported by the installed Streamlit version:
# codeBackgroundColor = "#FFFFFF"
# dataframeHeaderBackgroundColor = "#FAF8F3"
# dataframeBorderColor = "#E5DDD0"
```

Typography guidance:

- Prefer `font = "serif"` for the reading feel, or a Google Font such as Lora / Source Serif if the project already loads custom fonts.
- Keep UI chrome readable; do not shrink base text below comfortable defaults.
- Generous line length for prose: prefer `layout="centered"` for reading-heavy apps; use `"wide"` only for dense dashboards, with constrained prose blocks where needed.

## Optional CSS (only if theme gaps remain)

If you must inject CSS (e.g. scrollbar, subtle card radius), keep it minimal and variable-driven:

```css
:root {
  --paperwhite-bg: #F5F1E8;
  --paperwhite-bg-elevated: #FAF8F3;
  --paperwhite-text: #2C2416;
  --paperwhite-accent: #8B7355;
  --paperwhite-border: #E5DDD0;
  --paperwhite-shadow: rgba(44, 36, 22, 0.08);
  --paperwhite-radius: 8px;
  --paperwhite-transition: all 0.2s ease;
}
```

Rules of thumb:

- Soft radius `8px`–`12px`, warm low shadows only
- No harsh black borders; no neon / glow accents
- Buttons and inputs should inherit theme colors first
- Do not override every Streamlit class—target only confirmed gaps

## App-level polish

- Early `st.set_page_config` with a fitting title/icon
- Material icons in warm-neutral UI; avoid loud emoji sets
- Captions and help text for secondary information
- Status via badges / `st.success` / `st.error` that remain readable on paper backgrounds

## Verify

- Primary button label remains readable on `#8B7355`
- Sidebar, widgets, dataframe headers, and code blocks look coherent
- Light room / dim room readability is acceptable
- No large CSS fight with Streamlit's layout

## Deliver

- Theme applied via config (and minimal CSS only if needed)
- Short note of files changed and any version-specific theme keys skipped
