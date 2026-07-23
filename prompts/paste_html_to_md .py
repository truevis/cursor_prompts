#!/usr/bin/env python3

import pyperclip
import os
import html2text
import re

def clean_and_format_text(text):
    """Clean up and format the text content as proper Markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Don't wrap text
    
    # Check if it might be HTML content
    if re.search(r'<\w+[^>]*>', text) and re.search(r'</\w+>', text):
        # Try to convert as HTML
        try:
            return h.handle(text)
        except Exception as e:
            print(f"HTML conversion failed: {e}")
    
    # Process the text line by line to improve Markdown formatting
    lines = text.splitlines()
    formatted_lines = []
    in_code_block = False
    last_line_empty = True
    
    # Remove standalone "Copy" text that sometimes appears before code blocks
    lines = [line for line in lines if line.strip() != "Copy"]
    
    for i, line in enumerate(lines):
        line = line.rstrip()
        
        # Skip multiple consecutive empty lines
        if not line.strip():
            if not last_line_empty:
                formatted_lines.append("")
                last_line_empty = True
            continue
        else:
            last_line_empty = False
        
        # Convert section titles to proper Markdown headers
        # Look for all caps sections that might be headers
        if line.strip().isupper() and len(line.strip()) > 3 and i > 0 and not lines[i-1].strip():
            # This might be a header - look at following line to determine level
            level = 1  # Default to H1
            
            # If there's a following non-empty line with symbols like = or -, adjust level
            if i+1 < len(lines) and lines[i+1].strip() and all(c in '=-:' for c in lines[i+1].strip()):
                if '=' in lines[i+1]:
                    level = 1
                else:
                    level = 2
                # Skip the next line since it's part of the header formatting
                lines[i+1] = ''
            
            # Add the properly formatted Markdown header
            formatted_lines.append(f"{'#' * level} {line}")
            continue
        
        # Detect the start of a code block
        if line.strip() == "```" or (line.strip().startswith("```") and len(line.strip()) > 3):
            in_code_block = not in_code_block
            formatted_lines.append(line)
            continue
        
        if in_code_block:
            # Don't modify text inside code blocks
            formatted_lines.append(line)
            continue
        
        # Convert bullet points and numbered lists
        list_match = re.match(r'^(\s*)[-•*]\s+(.*)', line)
        if list_match:
            indent, content = list_match.groups()
            formatted_lines.append(f"{indent}* {content}")
            continue
        
        # Fix numbered lists
        num_list_match = re.match(r'^(\s*)(\d+)[\.\)]\s+(.*)', line)
        if num_list_match:
            indent, num, content = num_list_match.groups()
            formatted_lines.append(f"{indent}{num}. {content}")
            continue
        
        # Convert URL lines to markdown links if they stand alone
        if line.strip().startswith(('http://', 'https://')):
            formatted_lines.append(f"[{line.strip()}]({line.strip()})")
            continue
            
        # Process headers with colons (like "Title: Content")
        if ":" in line and not "://" in line:
            parts = line.split(":", 1)
            if len(parts[0].split()) <= 3 and parts[0].strip() and parts[0].isupper():
                # This looks like a header
                formatted_lines.append(f"## {parts[0].strip()}")
                if parts[1].strip():
                    formatted_lines.append(parts[1].strip())
                continue
        
        # Add the line as is
        formatted_lines.append(line)
    
    # Join the formatted lines
    formatted_text = "\n".join(formatted_lines)
    
    # Fix any remaining issues
    # Remove excess newlines (more than 2 consecutive)
    formatted_text = re.sub(r'\n{3,}', '\n\n', formatted_text)
    
    # Fix code blocks - make sure they have language hints
    formatted_text = re.sub(r'```\s*\n', '```\n', formatted_text)
    
    return formatted_text

def get_clipboard_content():
    """Get content from clipboard."""
    try:
        content = pyperclip.paste()
        if content:
            return clean_and_format_text(content)
        return ""
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        return ""

def save_to_markdown(content, filename="md.md"):
    """Save content to a markdown file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Content saved to {os.path.abspath(filename)}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    # Get content from clipboard
    content = get_clipboard_content()
    
    if content:
        # Print the content preview
        preview_length = min(500, len(content))
        print("\nClipboard content (preview):")
        print("-" * 40)
        print(content[:preview_length] + ("..." if len(content) > preview_length else ""))
        print("-" * 40)
        
        # Ask for filename
        default_filename = "md.md"
        user_filename = input(f"\nEnter filename to save as markdown (default: {default_filename}): ").strip()
        
        # Use default if no input
        filename = user_filename if user_filename else default_filename
        
        # Add .md extension if not provided
        if not filename.endswith('.md'):
            filename += '.md'
        
        # Save content to markdown file
        save_to_markdown(content, filename)
    else:
        print("No content found in clipboard.")

if __name__ == "__main__":
    main()
