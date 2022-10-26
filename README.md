# LAP 4 Code Challenge
Let’s face it, most developers are a bit lazy. One thing that can be really laborious is typing in very long URL’s so let's solve that problem! You are going to create a URL shortener.

To test an existing, free, URL shortener service, check out [Free URL Shortener](https://free-url-shortener.rb.gy/).

You will be working in pairs for this challenge and teaming up with another pair to give feedback via PR review.

## Requirements
- Users should be able to enter a url into an input box on your website's front page
- Your backend will then generate a shortened path at which a User can access their url
- You must implement Python in some capacity in this application
- Store this shortened path and it's longer counterpart in a database
- No login should be required to create a shortened URL
- If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to 
- If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL 

**Example**:
- User visits your site, `www.short.io`
- User enters `http://getfutureproof.co.uk/` to the provided input
- User receives a new, short URL eg. `www.short.io/u5o83` 
- User can now access the futureproof site via the new, short URL


## Timeline
- Tuesday PM & Wednesday AM: Work on challenge in pairs
#### Wednesday
- 1pm: It's lunchtime! All work to have been pushed to a GitHub repo with review requested from another pair.
- 2pm: Review the request sent to you by the other pair
- 3pm: Meet with the other pair to discuss the comments that have been made.
- 4pm: Take your feedback and use it to implement any changes and improvements.

## Tips
- Create a new repo on GitHub early and push a basic README.md
- Very early on, before you've pushed any more code to GitHub, [make a new branch on GitHub](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-and-deleting-branches-within-your-repository) called review/feedback/free-beer, whatever you like. Don’t push or merge anything to it, we’ll use it tomorrow for review purposes.
- When you find out who your review partners are, [add them as collaborators](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository)
- When ready to submit for review, make all final commits and push to your working branch
- Make a Pull Request ***to*** your review branch, ***from*** your working branch
- **Do not** merge this PR!
- Request review on your PR by adding your review partners as reviewers by clicking the cog next to 'Reviewers' on the pull request page
- Keep an eye out in your own email and/or [GitHub notifications](https://github.com/notifications?query=reason%3Areview-requested) to see when you have been requested to review another team's work!
