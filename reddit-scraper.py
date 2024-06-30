import praw
import csv

# Define your credentials
CLIENT_ID = 'vstM2xdDcE-R5ZCJfRQiAw'
CLIENT_SECRET = 'g7H871S_IAzRZpjBVQjYydbVSR1J4A'
USER_AGENT = 'stories_scraper 1.0 by /u/mrgoosee'

# Authenticate with Reddit
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Define the subreddit
subreddit_name = 'AmItheAsshole'

# Fetch top stories
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(limit=1000)

# Save the posts to a CSV file
with open('aita_top_posts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Text'])

    for post in top_posts:
        # Remove new lines from the text
        clean_text = post.selftext.replace('\n', ' ').replace('\r', ' ')
        writer.writerow([post.title, clean_text])

print("Posts have been saved to aita_top_posts.csv")
