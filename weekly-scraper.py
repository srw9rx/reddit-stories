import praw
import datetime as dt
import csv
import os
from tqdm import tqdm
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

# Authenticate with Reddit
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

# Define the subreddit
subreddit_name = 'AmItheAsshole'

# Define the path to the CSV file
file_path = 'aita_top_posts_by_week.csv'

# Function to fetch top posts for the past week using the Reddit API
def fetch_top_posts_for_past_week():
    top_posts = []
    subreddit = reddit.subreddit(subreddit_name)
    for post in tqdm(subreddit.top(time_filter='week', limit=10), desc='Fetching top posts for the past week'):
        if post.is_self:  # Ensure it's a self post
            top_posts.append((post.title, post.selftext.replace('\n', ' ').replace('\r', ' ')))
    return top_posts

# Get the current week range
def get_current_week_range():
    current_date = dt.datetime.now(dt.timezone.utc)
    start_date = current_date - dt.timedelta(days=current_date.weekday())  # Start of the week (Monday)
    end_date = start_date + dt.timedelta(days=6)  # End of the week (Sunday)
    return start_date.date(), end_date.date()

# Fetch the current week's posts
start_date, end_date = get_current_week_range()
week_label = f"{start_date} to {end_date}"

# Check existing weeks in the CSV file
existing_weeks = set()
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            existing_weeks.add(row[0])

# Fetch and update the CSV file with the current week's posts
if week_label not in existing_weeks:
    top_posts = fetch_top_posts_for_past_week()
    if top_posts:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if os.path.getsize(file_path) == 0:
                writer.writerow(['Week', 'Title', 'Text'])
            for title, text in top_posts:
                writer.writerow([week_label, title, text])
        print(f"CSV file updated with posts from the week: {week_label}")
    else:
        print(f"No posts found for the week: {week_label}")
else:
    print(f"Week {week_label} is already updated in the CSV file.")
