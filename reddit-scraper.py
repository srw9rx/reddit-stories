import praw
import datetime as dt

# Define your credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
USER_AGENT = 'your_user_agent'

# Authenticate with Reddit
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Define the subreddit and the timeframe
subreddit_name = 'AmItheAsshole'
timeframe = '3_months'

# Calculate the start time (3 months ago)
current_time = dt.datetime.utcnow()
start_time = current_time - dt.timedelta(days=90)

# Fetch top stories from the past 3 months
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(time_filter='all', limit=1000)

# Filter posts from the past 3 months
filtered_posts = [post for post in top_posts if dt.datetime.utcfromtimestamp(post.created_utc) > start_time]

# Print the top stories
for post in filtered_posts:
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"URL: {post.url}")
    print(f"Date: {dt.datetime.utcfromtimestamp(post.created_utc)}")
    print(f"Comments: {post.num_comments}")
    print('---')
