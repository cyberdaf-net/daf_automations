# Extract LinkedIn Posts

> Important: Use the Playwright MCP browser tools directly (mcp__playwright__*). 
> Do NOT write a Node.js script or install npm packages.
> Use Obsidian wikilink format for embedding images: ![[attachments/short-title-1.png]]
> Leave "# Related Notes" and "# Additional References" empty — these are for manual input.

Read `inputs/linkedin_posts.txt` to get the list of URLs.

Then use the Playwright browser tool to:

1. Navigate to https://www.linkedin.com/login
2. Log in using the LINKEDIN_EMAIL and LINKEDIN_PASSWORD environment variables
3. Wait for the home feed to confirm login succeeded
4. For each URL in the list, do the following one at a time:
   - Navigate to the post
   - Extract the author name, full post text, date, and any links found in the post body
   - Create a single line title focusing on the problem the author is suggesting and trying to solve
   - Create a short title with no more than 3 words to use as a reference for filenames (lowercase, hyphenated, e.g. `ai-knowledge-folder`)
   - If a file with the same short title already exists in `outputs/`, append a number to disambiguate (e.g. `ai-knowledge-folder-2.md`)
   - Select up to 10 keywords relevant to the post content, to make it easy to search
   - If the post contains one or more images:
     - Download each image and save it as a PNG to `outputs/attachments/` using the short title and image number as filename (e.g. `short-title-1.png`, `short-title-2.png`)
     - Convert to PNG if the original image is in a different format (e.g. jpg, webp)
     - Inspect each image to check if it contains text
     - If it does contain text, OCR the image and extract the text
   - If the post is unavailable, note it and skip
   - Create an individual markdown file in `outputs/` using the short title as filename (e.g. `short-title.md`) with this exact format:

---
keywords: [keyword1, keyword2, ...]
---
# Notes

## <single line title>

<full post text here, preserving the original line breaks, paragraphs, bullet points, emojis and formatting exactly as they appear on LinkedIn>

![[attachments/short-title-1.png]]

> <OCR extracted text from the image, if any. Omit this block entirely if the image has no text>

![[attachments/short-title-2.png]]

> <OCR extracted text from the second image, if any. Omit if no text>

---
# Related Notes


---
# External Sources
- [LinkedIn Post](<url>) - from [Author Name] - Published on: <date if visible>
- <any other links found in the post body, one per line>

---
# Additional References


   - If the markdown file was created successfully, remove that URL from `inputs/linkedin_posts.txt`
   - If the markdown file failed, leave the URL in `inputs/linkedin_posts.txt` and continue with the next URL

5. Once all posts have been processed, close the browser window.

6. If ALL posts were processed successfully with no errors, delete the `.playwright-mcp` folder.
   If ANY post failed or had an error, keep the `.playwright-mcp` folder for debugging.

Confirm when done and report how many posts succeeded and how many failed.