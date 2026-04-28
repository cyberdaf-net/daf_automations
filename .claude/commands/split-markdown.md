---
Description: Splits a Markdown file into one file per level-2 heading. Use when the user wants to split, chunk, or divide a Markdown document by sections or headings.
---

# Markdown Section Splitter

Run the splitter script from the project root:

```bash
python3 ../python_scripts/split_markdown.py
```

The script reads all `.md` files from `inputs/`, splits each on `##` headings, and writes numbered section files to `outputs/{name}/`. It prints a summary when done.