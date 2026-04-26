---
Description: Converts PDF files to Markdown, extracting text and images. Use when the user wants to convert, extract, or transform a PDF into Markdown or text format.
---

# PDF to Markdown Converter

## Global Rules

- Never ask for confirmation
- Use `pymupdf` (`pip install pymupdf`, import as `import fitz`) for all PDF operations
- Use `pytesseract` (`pip install pytesseract`) for OCR on images
- On error with a single file: log the error, skip it, continue

## Input Discovery

- Glob `inputs/*.pdf`
- If none found, print "No PDFs found in inputs/" and exit

## Output Structure

For each `inputs/{name}.pdf`:
```
outputs/{name}/
├── {name}.md
└── attachments/
    └── {name}-figure-{n}.png   # 1-indexed, only if images exist
```

## Extraction (single pass per page, in order)

Process each page using `page.get_text('dict')` to get all blocks sorted by (y0, x0).
Each block is either a **text block** or an **image block** — write them to the Markdown in the order they appear on the page.

**Text blocks:**

Before writing any text, compute the **modal font size** for the page (the most frequently occurring size across all spans). Use this as the baseline body size.

- span size ≥ baseline × 1.4 → `## `
- span size ≥ baseline × 1.15 → `### `
- otherwise → plain paragraph

This ensures headings are always relative to the document's own body text, regardless of absolute point sizes.

**Image blocks:**
- Skip images smaller than 50×50 px (decorative)
- Save as `attachments/{name}-figure-{n}.png`
- Run `pytesseract` OCR on the saved image
- Write to Markdown:
  ```
  ![[attachments/figure-{n}.png]]
  {ocr text, if any — as plain text beneath the image, not a blockquote}
  ```
- If OCR returns empty or whitespace, omit the text line

## Completion

Print a single summary line:
`Processed: N | Images: N | OCR'd: N | Skipped: N (<file>: <reason>, ...)`