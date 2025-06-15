#!/usr/bin/env python3

import os
from markitdown import MarkItDown

JS_DOC_FILES_LIST = "scripts/js_doc_files.txt"
MERGED_OUTPUT_FILE = "_posts/plotly_js/javascript_merged_docs.md"

import tempfile

def convert_html_to_markdown(html_content):
    """Converts HTML content to Markdown using markitdown."""
    temp_file_path = None  # Initialize to ensure it's always defined
    try:
        # Create a temporary file to store HTML content
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.html', encoding='utf-8') as temp_f:
            temp_f.write(html_content)
            temp_file_path = temp_f.name

        converter = MarkItDown()
        # Pass the filepath to the convert method
        result = converter.convert(temp_file_path)
        markdown_content = result.text_content
        return markdown_content
    except Exception as e:
        print(f"Error converting HTML to Markdown: {e}")
        return None
    finally:
        if temp_file_path:  # Check if temp_file_path was assigned
            try:
                os.remove(temp_file_path)
            except OSError as e:
                print(f"Error deleting temporary file {temp_file_path}: {e}")

def read_file_content(filepath):
    """Reads content from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def main():
    """Main function to merge JavaScript documentation files."""
    all_markdown_content = []

    # Read the list of file paths
    file_paths_content = read_file_content(JS_DOC_FILES_LIST)
    if not file_paths_content:
        return

    file_paths = [line.strip() for line in file_paths_content.splitlines() if line.strip()]

    for filepath in file_paths:
        print(f"Processing file: {filepath}")
        content = read_file_content(filepath)
        if content is None:
            continue

        _, extension = os.path.splitext(filepath)

        if extension == ".html":
            markdown_content = convert_html_to_markdown(content)
            if markdown_content:
                all_markdown_content.append(markdown_content)
            else:
                print(f"Skipping file due to conversion error: {filepath}")
        elif extension == ".md":
            all_markdown_content.append(content)
        else:
            print(f"Skipping file with unsupported extension: {filepath}")
            continue

        all_markdown_content.append("\n") # Add newline for separation

    # Concatenate all processed content
    merged_content = "".join(all_markdown_content)

    # Save the merged content
    try:
        os.makedirs(os.path.dirname(MERGED_OUTPUT_FILE), exist_ok=True)
        with open(MERGED_OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(merged_content)
        print(f"Successfully merged documents into {MERGED_OUTPUT_FILE}")
    except Exception as e:
        print(f"Error writing merged file: {e}")

if __name__ == "__main__":
    main()
