import praw
import csv
from tqdm import tqdm
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT

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

    for post in tqdm(top_posts, 'scraping top posts:'):
        # Remove new lines from the text
        clean_text = post.selftext.replace('\n', ' ').replace('\r', ' ')
        writer.writerow([post.title, clean_text])

print("Posts have been saved to aita_top_posts.csv")
