1. Navigate to https://www.linkedin.com/login
2. Log in using the LINKEDIN_EMAIL and LINKEDIN_PASSWORD environment variables
3. Wait for the home feed to confirm login succeeded
4. For each URL in the list:
   - Navigate to the post
   - Extract the author name, full post text, and any visible date
   - If the post contains an image:
     - Download it and save it to `outputs/attachments/` with a filename based on the author name and post number (e.g. `john-doe-1.jpg`)
     - Inspect the image to check if it contains text
     - If it does contain text, OCR the image and extract the text
   - If the post is unavailable, note it and skip
5. Write all results to `outputs/posts.md`. For each post use this format:

# [Author Name]
**URL:** <url>  
**Date:** <date if visible>

<full post text here, preserving the original line breaks, paragraphs, bullet points, emojis and formatting exactly as they appear on LinkedIn>

![image](attachments/author-name-1.jpg)

> <OCR extracted text from the image, if any. If the image has no text, omit this block entirely>

<br>

---

<br>

6. Close the browser once posts.md has been written.

7. If ALL posts were processed successfully with no errors, delete the `.playwright-mcp` folder.
   If ANY post failed or had an error, keep the `.playwright-mcp` folder for debugging.

Confirm when done and let me know whether the debug folder was kept or deleted.