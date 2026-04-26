---
Description: Splits a Markdown file into one file per level-2 heading. Use when the user wants to split, chunk, or divide a Markdown document by sections or headings.
---

# Markdown Section Splitter

## Behaviour

- Process every `.md` file in `inputs/`
- For each file, create `outputs/{name}/`
  - Split on `##` headings; ignore content before the first `##`
  - Save each section as `{nn} {name[:10]} - {Heading Text}.md` inside that folder
    (e.g. `outputs/LongFileName/01 LongFileNa - Introduction.md`)
- Zero-pad counter to 2 digits; expand to 3 if sections exceed 99

## Edge Cases

- No `##` headings → copy file unchanged to `outputs/{name}/` with a warning
- Heading text contains `/` or `\` → replace with `-`

## Implementation

Use Python (stdlib only). Read each file, split on lines starting with `## `, write sections.