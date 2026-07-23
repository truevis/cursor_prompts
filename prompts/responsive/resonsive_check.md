Do this so your web app doesn't look stupid to your users on desktop AND mobile. Responsiveness is key!



Give this to your agent:

"You are acting as a senior frontend engineer, responsive design specialist and visual QA auditor.



Your task is to inspect the entire application, identify every real responsiveness issue, fix each confirmed issue in the codebase, and verify that the fixes work across supported screen sizes.



Do not give me a list of generic responsive design recommendations.



Do not only inspect screenshots or read the code.



Run the application, interact with every important screen, reproduce the layout failures, trace them to the responsible component or CSS rule, implement the smallest reliable fix, and retest the affected flows.



Primary objective



Ensure that every screen remains usable, readable and visually coherent across mobile, tablet, laptop and large desktop layouts.



The application must not merely “fit” on smaller screens. Its hierarchy, interaction model, spacing, content priority and controls must adapt appropriately to the available space.



Step 1: Map the responsive surface area



Identify:

\- Every route and major application screen

\- Shared layouts, shells, sidebars, headers and navigation components

\- Modals, drawers, popovers, dropdowns and tooltips

\- Forms, settings pages and onboarding flows

\- Tables, dashboards, cards and data-heavy views

\- Editors, canvases, previews and split-screen interfaces

\- Authentication screens

\- Empty, loading, error and success states

\- Components reused across multiple pages

\- Screens shown only under particular roles, plans or application states



Create a testing inventory before making changes so important screens are not skipped.



Step 2: Test across viewport sizes



Test each important screen at these viewport widths at minimum:



\- 320px

\- 360px

\- 375px

\- 390px

\- 414px

\- 480px

\- 768px

\- 820px

\- 1024px

\- 1280px

\- 1440px

\- 1920px



Also test:



\- Portrait and landscape orientations

\- Short viewport heights

\- Browser zoom at 80%, 100%, 125%, 150% and 200%

\- Device pixel ratios where possible

\- Mobile browser safe areas

\- On-screen keyboard appearance

\- Long pages with substantial scrolling

\- Pages with little or no content

\- Pages with maximum realistic content



Do not assume that passing at one mobile width means the screen is responsive.



Test intermediate widths and resize continuously to catch breakpoint gaps, snapping issues and layout instability.



Step 3: Stress the content



Test layouts using realistic worst-case content, including:



\- Very long page titles

\- Long names and email addresses

\- Long button labels

\- Long navigation labels

\- Long URLs

\- Long unbroken strings

\- Large numbers

\- Negative values

\- Multi-line validation messages

\- Large tables

\- Many tags or chips

\- Empty values

\- Missing images

\- Wide images

\- Tall images

\- Different image aspect ratios

\- Large uploaded filenames

\- Localised text that is significantly longer than English

\- User-generated content with unexpected formatting



Do not fix responsiveness by hiding important information without a deliberate product reason.



Step 4: Inspect common failure modes



Attempt to reproduce and fix:



\- Layout and overflow



Horizontal page scrolling

Content wider than the viewport

Fixed-width elements that do not shrink

Images, videos, charts or canvases overflowing their containers

Tables breaking page width

Cards extending beyond the screen

Grid columns becoming too narrow

Elements overlapping

Text colliding with icons

Content clipped by overflow: hidden

Broken sticky or fixed positioning

Incorrect viewport height usage

Layouts failing when browser chrome changes height

Modals taller or wider than the viewport

Drawers that cannot be fully accessed

Dropdowns and popovers rendering off-screen



\- Typography



Text becoming too small to read

Headings wrapping awkwardly

Single words creating overflow

Excessively long line lengths on desktop

Truncated text without a way to access the full value

Labels becoming detached from their inputs

Uneven vertical rhythm after wrapping

Buttons growing unpredictably because of text length



\- Navigation



Desktop navigation failing to adapt on smaller screens

Mobile navigation being difficult to open or close

Navigation covering page content

Active states disappearing

Important actions becoming inaccessible

Breadcrumbs overflowing

Tabs extending beyond the viewport

Horizontal tab scrolling without visible affordance

Back navigation becoming unclear on mobile



\- Forms



Inputs extending beyond their container

Multi-column forms remaining cramped on mobile

Labels, help text and errors overlapping

Buttons becoming too small or difficult to tap

Action buttons disappearing beneath the mobile keyboard

Fixed footers covering form fields

Select menus and date pickers rendering off-screen

Inline form actions wrapping into unusable layouts

Validation messages causing layout jumps

Password managers or autofill changing field dimensions



\- Tables and dense data



For every table, decide and implement the correct responsive behaviour rather than forcing one global solution.



Use the most appropriate pattern:



Horizontal scrolling

Priority-based column hiding

Responsive card conversion

Expandable rows

Stacked metadata

Condensed column labels

Separate mobile detail views



Preserve access to important information and row actions.



Verify that sticky headers, sorting, selection and pagination remain usable.



Interaction and touch



\- Tap targets smaller than approximately 44 by 44 pixels

\- Controls positioned too close together

\- Hover-only actions with no touch alternative

\- Tooltips containing essential information

\- Drag-and-drop interactions without a mobile fallback

\- Context menus that cannot be opened on touch devices

\- Swipe areas conflicting with browser gestures

\- Fixed controls hidden behind safe-area insets

\- Focus states cut off by container overflow



Visual hierarchy



Desktop spacing copied directly onto mobile

Excessive empty space

Content becoming overly compressed

Important actions appearing below secondary content

Cards stacking in the wrong order

Side content appearing before primary content

Repeated page titles consuming too much vertical space

Mobile screens feeling like shrunken desktop screens

Large desktop layouts becoming too sparse

Content stretching across unreadably wide containers



Step 5: Inspect implementation quality



For every confirmed issue, inspect the underlying implementation.



Look for:



Hard-coded widths and heights

Excessive absolute positioning

Fragile negative margins

Arbitrary pixel offsets

Unnecessary min-width values

Incorrect flex shrink or grow behaviour

Missing min-width: 0

Missing max-width

Grid definitions that cannot collapse safely

Components depending on viewport-specific magic numbers

Inconsistent breakpoint definitions

Conflicting media queries

Incorrect container queries

CSS specificity conflicts

Duplicate responsive rules

JavaScript-based viewport logic where CSS would be more reliable

Hydration mismatches caused by viewport detection

Components reading window.innerWidth unsafely

Device detection used in place of capability or layout detection



Prefer resilient layout systems using flexbox, grid, intrinsic sizing, fluid typography, container queries and content-driven breakpoints where appropriate.



Do not add unnecessary breakpoints.



Do not solve every issue with a one-off media query.



Fix the underlying layout model whenever possible.



Step 6: Implement fixes



For each confirmed issue:



Reproduce the issue

Identify the responsible component

Identify the exact CSS, layout or rendering cause

Capture the failing state

Implement the smallest safe fix

Verify the fix at the failing viewport

Check nearby viewport widths

Check that desktop behaviour has not regressed

Check every other screen using the same shared component

Add or update automated coverage where practical



Do not redesign unrelated parts of the application.



Do not alter product behaviour unless the current responsive behaviour makes the feature unusable.



Do not hide controls merely to make the layout look cleaner.



Do not use !important unless there is a documented and unavoidable reason.



Do not introduce duplicated mobile and desktop implementations unless one responsive component would be materially more complex or less accessible.



Step 7: Verify accessibility alongside responsiveness



Confirm that:



Content reflows at 200% zoom without loss of functionality

Keyboard focus remains visible

Focus order follows the visual layout

Reordered content still has a logical reading order

Touch targets remain usable

Text remains readable

Controls are not clipped

Modal content can be reached by keyboard

Screen reader labels remain accurate after responsive transformations

Hidden content is actually removed from assistive technology when appropriate

Responsive tables retain meaningful headers and relationships

Orientation changes do not cause loss of content or functionality



Step 8: Add regression coverage



Where the project supports automated browser testing, add responsive regression tests for critical screens.



At minimum, cover:



One small mobile viewport

One large mobile viewport

One tablet viewport

One desktop viewport

One large desktop viewport



Tests should check meaningful failures, including:



No unexpected horizontal document overflow

Primary navigation is usable

Primary actions are visible

Modals remain inside the viewport

Forms remain accessible

Critical content is not hidden

Tables use their intended responsive behaviour

No severe element overlap

Mobile and desktop navigation states render correctly



Use visual regression snapshots where available, but do not rely on screenshots alone. Include behavioural assertions.



Required output



After completing the work, provide:



1\. Screens tested



List every route, component and application state reviewed.



2\. Confirmed issues



For each issue include:



Issue title

Severity

Affected route or component

Failing viewport

Reproduction steps

Root cause

Code changed

Fix implemented

Verification performed



3\. Files changed



List each modified file and explain why it changed.



4\. Remaining limitations



Include only issues that could not be fixed safely, with the precise reason.



5\. Responsive release verdict



Choose one:



Ready to release

Ready with minor known limitations

Not ready to release



Base the verdict on observed and retested behaviour.



Completion criteria



Do not consider the task complete until:



Every major route has been tested

Every shared layout has been tested

Confirmed issues have been fixed

Fixes have been retested across adjacent viewport widths

Mobile and desktop regressions have been checked

There is no unexplained horizontal page overflow

Primary actions remain accessible

Forms remain usable with the mobile keyboard open

Modals, drawers and overlays remain inside the viewport

Dense content has an intentional mobile treatment

The final report distinguishes reproduced failures from assumptions



Do not tell me what you would test.



Perform the testing, make the fixes, and show what changed."

