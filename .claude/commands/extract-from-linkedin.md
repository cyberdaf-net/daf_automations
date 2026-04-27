# Summarize LinkedIn Posts

> Important: Use the Playwright MCP browser tools directly (mcp__playwright__*). 
> Do NOT write a Node.js script or install npm packages.

Read `inputs/linkedin_posts.txt` to get the list of URLs.

Then use the Playwright browser tool to:

1. Navigate to https://www.linkedin.com/login
2. Log in using the LINKEDIN_EMAIL and LINKEDIN_PASSWORD environment variables
3. Wait for the home feed to confirm login succeeded
4. For each URL in the list:
   - Navigate to the post
   - Extract the author name, full post text, and any visible date
   - If the post is unavailable, note it and skip
5. Write all results to `outputs/summaries.md` using this format:

**Author**: [Author Name]
**URL:** <url>  
**Date:** <date if visible>

<full post text here, preserving the original line breaks, paragraphs, bullet points, emojis and formatting exactly as they appear on LinkedIn>

![image](images/author-name-1.jpg)

<br>

6. If ALL posts were processed successfully with no errors, delete the `.playwright-mcp` folder.
   If ANY post failed or had an error, keep the `.playwright-mcp` folder for debugging.

Confirm when done and let me know whether the debug folder was kept or deleted.