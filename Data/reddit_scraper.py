# -*- coding: utf-8 -*-
"""Reddit_Scraper.ipynb
"""

import praw
import time
import pandas as pd
from datetime import datetime


# Initialize a Reddit instance with your API credentials
reddit = praw.Reddit(
    client_id='XXXXX',
    client_secret='XXXX',
    user_agent='XXXX',
)

# Specify the subreddit you want to scrape
subreddit_name = 'techsupport'

# Get the subreddit object
subreddit = reddit.subreddit(subreddit_name)

# Define the number of top posts you want to scrape
num_posts_to_scrape = 2000

# Create a list to store post and comment data
combined_data = []

# Loop through the top posts in the subreddit
for submission in subreddit.top(limit=num_posts_to_scrape):
    # Create a dictionary to store post information
    post_info = {
        'Type': 'Post',
        'Title': submission.title,
        'URL': submission.url,
        'Content': submission.selftext,
    }
    combined_data.append(post_info)
    time.sleep(2)


    submission.comments.replace_more(limit=None)
    #print(submission.comments)
    for comment in submission.comments.list():
        comment_info = {
            'Type': 'Comment',
            'Post Title': submission.title,
            'Content': comment.body,
            'Post Date': str(datetime.fromtimestamp(comment.created_utc)) ,
            'Post user': comment.author,
        }
        combined_data.append(comment_info)


    # Create a DataFrame from the collected data
combined_df = pd.DataFrame(combined_data)

# Save the DataFrame to an Excel file
combined_df.to_excel('reddit_data.xlsx', index=False)

