from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import api_requests
from data_base_tables import Base, Twitter, Reddit

engine = create_engine('sqlite:///discover_more.db', echo=False)

# Creating a table for all the things that use Base
Base.metadata.create_all(engine)

# Making a Session class
Session = sessionmaker(bind=engine)
session = Session()

# getting objects from the api_requests
user_tweets = api_requests.UserApiRequest()
user_reddit = api_requests.RedditAPIRequest()

def call_get_tweets():
    # getting the tweets and saving them
    user_tweets.get_tweets()
    save_twitter()

def call_get_reddit():
    # getting the results from Reddit and saving them
    user_reddit.search_reddit()
    save_reddit()

def save_twitter():
    # saving each tweet, user name, and date of tweet to the database
    counts = len(user_tweets.screen_name)
    count = 0
    while count != counts:
        USER_NAME = user_tweets.screen_name[count]
        DATE = user_tweets.date_tweet[count]
        TWEET_TEXT = user_tweets.tweet_list[count]
        count += 1

        record1 = Twitter(user_name=USER_NAME, tweet_text=TWEET_TEXT, tweet_date=DATE)

        save_session = Session()

        save_session.add(record1)

        save_session.commit()

        save_session.close()

def save_reddit():
    # saving each subreddit title and url to the database
    counts = len(user_reddit.title)
    count = 0
    while count != counts:
        SUBREDDIT_TITLE = user_reddit.title[count]
        SUBREDDIT_URL = user_reddit.urls[count]
        count += 1

        record1 = Reddit(subreddit_title=SUBREDDIT_TITLE, url_subreddit=SUBREDDIT_URL)

        save_session = Session()

        save_session.add(record1)

        save_session.commit()

        save_session.close()
