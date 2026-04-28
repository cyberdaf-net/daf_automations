---
Description: Converts PDF files to Markdown, extracting text and images. Use when the user wants to convert, extract, or transform a PDF into Markdown or text format.
---

# PDF to Markdown Converter

Run the converter script:

```bash
python3 .claude/python_scripts/convert_pdfs_to_md.py
```

The script reads all `.pdf` files from `inputs/`, extracts text and images (with OCR), and writes `outputs/{name}/{name}.md` with an `attachments/` subfolder for images. It prints a summary when done.