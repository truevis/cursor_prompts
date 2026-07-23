---
name: streamlit-hot-reload
description: Use importlib.reload to force Streamlit to pick up local Python module changes on rerun. Use when editing helpers imported by a Streamlit app and changes do not appear after save.
---

# Streamlit hot reload with `importlib.reload`

Streamlit keeps imported modules in `sys.modules`. Edits to local helper modules may not appear on rerun. During development, reload local modules before importing names from them.

## When to use

- App imports functions from local packages/modules
- You change those modules and the UI still runs old code
- You are not using a process restart workflow

Skip in production, or gate behind a debug flag.

## Pattern

```python
import importlib

import streamlit as st

# Import local modules as modules first
import my_module
import helpers.data_processing
import config.settings

# Force reload so reruns see latest source
importlib.reload(my_module)
importlib.reload(helpers.data_processing)
importlib.reload(config.settings)

# Then import callables/constants from the reloaded modules
from my_module import my_function
from helpers.data_processing import process_data
from config.settings import DEFAULT_VALUE
```

## Complete example

```python
import importlib

import streamlit as st

# --- Hot reloading (development) ---
import helpers
import config
import data_processing
import ui_components

importlib.reload(helpers)
importlib.reload(config)
importlib.reload(data_processing)
importlib.reload(ui_components)

from helpers import helper_function
from config import APP_CONFIG
from data_processing import process_data
from ui_components import render_dashboard

# App code continues...
```

## Best practices

1. Reload **local** modules only—never pandas, streamlit, etc.
2. Place reload blocks near the top of the entry script, before using imported functions.
3. Reload order: import module → `importlib.reload(module)` → `from module import name`.
4. Reload every local module that owns functions you call from the app entrypoint.
5. Prefer a flag for production:

```python
import os

if os.getenv("STREAMLIT_DEV_RELOAD") == "1":
    importlib.reload(helpers)
```

## Notes

- `importlib.reload()` only works on modules already imported.
- Reloading on every rerun is intentional for dev freshness; it has a cost—keep it off in prod.
- If reloads get fragile (circular imports, caches), restart the Streamlit process instead of stacking more reload hacks.
