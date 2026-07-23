# Responsive check (Streamlit-first)

Act as a senior frontend engineer and visual QA auditor for this Streamlit app.

Inspect the running app, find real responsiveness issues, fix confirmed issues with the smallest reliable change, and retest. Do not deliver a generic responsive-design lecture. Do not stop at reading code or screenshots alone.

## Constraints

- Preserve product behavior unless the current layout makes a feature unusable.
- Prefer Streamlit layout APIs (`st.columns`, containers, sidebar, `layout` in `st.set_page_config`, dataframe column config) over one-off media-query CSS.
- Do not hide important information only to “look clean.”
- Do not start `streamlit run` unless the app is not already running; check the terminal for errors.
- Follow `cursorrules.md`.

## Streamlit-specific failure modes (check these first)

- Too many columns on narrow widths (aim ≤4; stack or reduce on mobile)
- Sidebar crowding: filters/nav OK; main charts/tables not
- `layout="wide"` content stretching unreadably; prose without a max readable width
- Dataframes/tables forcing horizontal page scroll with no intentional pattern
- Charts/images overflowing or shrinking into illegibility
- `st.tabs` / button rows wrapping into unusable clusters
- `st.dialog` / expanders / popovers clipped or taller than the viewport
- Forms with actions covered by mobile keyboard or sticky footers
- Metric/column strips that look fine on desktop but collapse into noise on phones
- Custom CSS with fixed `px` widths, `min-width`, or absolute positioning that breaks reflow
- Touch targets effectively smaller than ~44×44px for primary actions

## Step 1 — Inventory

List routes/pages (`pages/`, `st.navigation`), shared layout/sidebar, dialogs, forms, tables, charts, auth/empty/loading/error states, and role-gated screens. Build a short test inventory before fixing.

## Step 2 — Viewports

Exercise each important screen at least at: **320, 375, 414, 768, 1024, 1440, 1920** CSS px.

Also check: short heights, 200% zoom, landscape, long vs empty content, and continuous resize (breakpoint gaps). Passing at one phone width is not enough.

## Step 3 — Content stress

Use realistic worst cases: long titles/labels/emails/URLs, large tables, many chips, missing/wide images, long validation messages, non-English length expansion. Keep access to critical data and row actions.

## Step 4 — Fix approach

For each confirmed issue:

1. Reproduce at a failing width  
2. Trace to Streamlit layout/theme/CSS/component  
3. Apply the smallest fix (column ratios, stack, dataframe config, theme/layout, targeted CSS)  
4. Retest failing width, neighbors, and desktop regression  
5. Check other pages sharing the same layout  

Prefer intentional table patterns: horizontal scroll inside the widget, priority columns, expandable rows, or a mobile detail view—not one global hack.

## Step 5 — Accessibility with responsiveness

Confirm: reflow at 200% zoom, visible focus, logical order after stacking, usable touch targets, modals reachable, tables keep meaningful headers, no content loss on orientation change.

## Required report

1. **Screens tested** — routes/states reviewed  
2. **Confirmed issues** — title, severity, screen, viewport, repro, root cause, fix, verification  
3. **Files changed** — path + why  
4. **Remaining limitations** — only what could not be fixed safely  
5. **Verdict** — Ready / Ready with minor limitations / Not ready  

## Done when

Major routes and shared layouts tested; confirmed issues fixed and retested; no unexplained document-level horizontal scroll; primary actions and forms usable on small screens; dense data has an intentional mobile treatment; report separates evidence from assumptions.
