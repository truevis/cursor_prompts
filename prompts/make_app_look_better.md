# Make this Streamlit app look better

You are improving the visual polish and UX of this Streamlit app. Prefer Streamlit-native theming and layout APIs over large custom CSS. Preserve all existing functionality.

## Constraints

- Do not redesign the product or add new features.
- Prefer `.streamlit/config.toml` for colors/fonts; use CSS only for gaps theme cannot cover.
- Prefer Material icons (`:material/name:`) over emoji clutter.
- Keep the sidebar for navigation and global filters only.
- Assume the app is already running and will rerun on save; do not start Streamlit unless asked.
- Follow `cursorrules.md` and load the Streamlit design/theme/layout skills when available.

## Do this (in order)

1. **Page identity**
   - Set `st.set_page_config` early: clear `page_title`, relevant `page_icon` (Material icon or image), and appropriate `layout` (`"centered"` for focused apps, `"wide"` for dense dashboards).
   - Add `st.logo(...)` when a logo asset exists or can be added without inventing brand assets.

2. **Theme first**
   - Put cohesive colors and fonts in `.streamlit/config.toml` (`primaryColor`, backgrounds, `textColor`, borders, optional chart/dataframe colors).
   - Choose a palette that fits the app's domain; ensure WCAG AA contrast for body text and primary buttons (primary must contrast with white label text).

3. **Typography and hierarchy**
   - Use clear header levels; sentence case for labels and buttons.
   - Prefer Streamlit heading/caption APIs over raw HTML for text hierarchy.
   - Avoid heavy `st.divider()` usage; rely on spacing and section headers.

4. **Layout**
   - Cap columns at ~4; use width ratios; set `vertical_alignment` where needed.
   - Use `st.container(horizontal=True)` for button groups instead of fragile column hacks.
   - Keep main content in the main pane; do not park charts/tables in the sidebar.

5. **Controls and feedback**
   - Make primary actions obvious; secondary actions quieter.
   - Style status with `st.badge` / badge markdown, not ad-hoc colored HTML.
   - Ensure success/error/warning messages are clear and next to the action that caused them.

6. **Responsive sanity**
   - Check narrow and wide layouts: stacked columns, readable tables/charts, usable sidebar, no horizontal page scroll.
   - For dense tables, choose an intentional mobile pattern (scroll, fewer columns, or detail view)—do not hide critical data casually.
   - For a deeper pass, use `responsive_check.md`.

7. **Motion**
   - Keep motion minimal. Prefer Streamlit's built-in feedback (spinners, status, fragments) over decorative CSS animation.

## Avoid

- Purple-on-white / generic “AI dashboard” gradients unless they match an existing brand.
- Card spam (borders/shadows/radius) that does not aid interaction.
- Large injected CSS that fights the theme.
- Emoji-heavy navigation or icon salad.

## Deliver

- Apply the changes in the codebase.
- Briefly list what changed and which files were touched.
- Note any polish that needs a brand asset (logo/favicon) the repo does not have.
