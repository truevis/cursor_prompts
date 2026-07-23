# Prevent LaTeX rendering in Streamlit

Streamlit treats `$...$` as LaTeX. When showing LLM or user text that may contain dollar amounts, neutralize `$` at **display time only**.

## Utility

```python
FULLWIDTH_DOLLAR = "\uFF04"  # ＄ — looks like $, not a LaTeX delimiter


def for_streamlit_display(text: str | None) -> str:
    """Replace ASCII $ so Streamlit does not render LaTeX. Display-only."""
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    return text.replace("$", FULLWIDTH_DOLLAR)
```

## Apply only at render time

| Safe to transform | Do **not** transform |
|-------------------|----------------------|
| `st.markdown(...)`, `st.write(...)`, chat message UI | Session-state / DB history |
| Streaming chunks as they are shown | Downloads (MD, CSV, Word, etc.) |
| Captions and help text shown in the UI | Copied “raw” export payloads |

### Chat

```python
st.chat_message("assistant").markdown(for_streamlit_display(reply))
```

### Streaming

```python
placeholder = st.empty()
acc = []
for chunk in stream:
    acc.append(chunk)
    placeholder.markdown(for_streamlit_display("".join(acc)))
# store "".join(acc) with original "$" if you persist history
```

### Direct output

```python
st.write(for_streamlit_display(model_text))
```

## Why

- Prevents accidental math rendering in business copy and prices  
- Keeps stored/exported text accurate with ASCII `$`  
- Works for streaming and non-streaming UI paths  

## Checklist

- [ ] Helper exists once (shared util), not copy-pasted per page  
- [ ] Used on UI paths that show model/user free text  
- [ ] History, logs, and downloads still use original `$`  
- [ ] Non-string inputs handled safely  
