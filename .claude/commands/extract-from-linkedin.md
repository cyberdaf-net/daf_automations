# Summarize LinkedIn Posts

> Important: Use the Playwright MCP browser tools directly (mcp__playwright__*). 
> Do NOT write a Node.js script or install npm packages.

Read `inputs/linkedin_posts.txt` to get the list of URLs.

Then use the Playwright browser tool to:

1. Navigate to https://www.linkedin.com/login
2. Log in using the LINKEDIN_EMAIL and LINKEDIN_PASSWORD environment variables
3. Wait for the home feed to confirm login succeeded
4. For each URL in the list, do the following one at a time:
   - Navigate to the post
   - Extract the author name, full post text, and any visible date
   - If the post contains an image:
     - Download it and save it as a PNG to `outputs/attachments/` with a filename based on the author name and post number (e.g. `john-doe-1.png`)
     - Convert to PNG if the original image is in a different format (e.g. jpg, webp)
     - Inspect the image to check if it contains text
     - If it does contain text, OCR the image and extract the text
   - If the post is unavailable, note it and skip
   - Create an individual markdown file for the post in `outputs/` using the author name and date as filename (e.g. `john-doe-2026-04-27.md`) using this format:

# [Author Name]
**URL:** <url>  
**Date:** <date if visible>

<full post text here, preserving the original line breaks, paragraphs, bullet points, emojis and formatting exactly as they appear on LinkedIn>

![image](attachments/author-name-1.jpg)

> <OCR extracted text from the image, if any. If the image has no text, omit this block entirely>

   - If the markdown file was created successfully, remove that URL from `inputs/linkedin_posts.txt`
   - If the markdown file failed, leave the URL in `inputs/linkedin_posts.txt` and continue with the next URL

5. Once all posts have been processed, close the browser window.

6. If ALL posts were processed successfully with no errors, delete the `.playwright-mcp` folder.
   If ANY post failed or had an error, keep the `.playwright-mcp` folder for debugging.

Confirm when done and report how many posts succeeded and how many failed.