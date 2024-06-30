import praw
import datetime as dt
import csv
import os

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

# Define the path to the CSV file
file_path = 'aita_top_posts_by_week.csv'

# Function to get top posts for a given week
def fetch_top_posts_for_week(start_date, end_date):
    top_posts = []
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.top(time_filter='week', limit=1000):
        post_time = dt.datetime.fromtimestamp(post.created_utc, dt.timezone.utc)
        if start_date <= post_time < end_date:
            top_posts.append((post.title, post.selftext.replace('\n', ' ').replace('\r', ' ')))
        if len(top_posts) >= 5:
            break
    return top_posts

# Function to get week ranges for the past 52 weeks
def get_week_ranges():
    week_ranges = []
    current_date = dt.datetime.now(dt.timezone.utc)
    for i in range(52):
        end_date = current_date - dt.timedelta(weeks=i)
        start_date = end_date - dt.timedelta(days=7)
        week_ranges.append((start_date, end_date))
    return week_ranges

# Check existing weeks in the CSV file
existing_weeks = set()
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            existing_weeks.add(row[0])

# Fetch and update the CSV file with missing weeks
new_data = []
week_ranges = get_week_ranges()
for start_date, end_date in week_ranges:
    week_label = f"{start_date.date()} to {end_date.date()}"
    if week_label not in existing_weeks:
        top_posts = fetch_top_posts_for_week(start_date, end_date)
        for title, text in top_posts:
            new_data.append([week_label, title, text])

if new_data:
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if os.path.getsize(file_path) == 0:
            writer.writerow(['Week', 'Title', 'Text'])
        writer.writerows(new_data)
    print("CSV file updated with missing weeks.")
else:
    print("No updates needed. All weeks are up to date.")
