# Summarize LinkedIn Posts

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

---
## [Author Name]
**URL:** <url>
**Date:** <date if visible>
**Summary:** <2-3 sentence summary of the post>
---

Confirm when done.