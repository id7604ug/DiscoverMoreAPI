from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import api_requests
from data_base_tables import Base, Twitter, Reddit, Youtube, RedditTrending

engine = create_engine('sqlite:///discover_more.db', echo=False)

# Creating a table for all the things that use Base
Base.metadata.create_all(engine)

# Making a Session class
Session = sessionmaker(bind=engine)
session = Session()

# getting objects from the api_requests
user_tweets = api_requests.UserApiRequest()
user_reddit = api_requests.RedditAPIRequest()
user_youtube = api_requests.YoutubeAPIRequest()

def call_get_tweets():
    # getting the tweets and saving them
    user_tweets.get_tweets()
    save_twitter()

# Function for searching all APIs (twitter)
def call_search_all_twitter(search_string):
    user_tweets.search_using_string(search_string)
    save_twitter()
    return 'done'

def call_get_reddit():
    # getting the results from Reddit and saving them
    user_reddit.search_reddit()
    save_reddit()

# Function for searching all APIs (reddit)
def call_search_all_reddit(search_string):
    user_reddit.search_using_string(search_string)
    save_reddit()
    return 'done'

def call_get_youtube():
    # getting the results from youtube and saving them
    user_youtube.search_youtube()
    save_youtube()

# Function for searching all APIs (youtube)
def call_search_all_youtube(search_string):
    user_youtube.search_using_string(search_string)
    save_youtube()
    return 'done'

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

def save_youtube():
    # saving each video name, channel, and url to the database
    counts = len(user_youtube.video_names)
    count = 0
    while count != counts:
        VIDEO_NAME = user_youtube.video_names[count]
        CHANNEL = user_youtube.channels[count]
        YOUTUBE_URL = user_youtube.urls[count]
        count += 1

        record1 = Youtube(video_names=VIDEO_NAME, channels=CHANNEL, url_youtube=YOUTUBE_URL)

        save_session = Session()

        save_session.add(record1)

        save_session.commit()

        save_session.close()


def save_trending_reddit_news():
    trend_news = user_reddit.reddit_trending
    for news in trend_news:
        trends = RedditTrending(reddit_trending_news=news)
        save_session = Session()
        save_session.add(trends)
        save_session.commit()
        save_session.close()

def view_all_saved_twitter(user_choice):
    # viewing all the records
    search_session_twitter = Session()
    try:
         twitter = search_session_twitter.query(Twitter).all()
         row_count = search_session_twitter.query(Twitter).filter(Twitter.id > 0).count()
         count = 0
         while count != row_count:
             if user_choice == '1':
                 print('*', twitter[count].user_name)
                 count += 1
             elif user_choice == '2':
                 print('*', twitter[count].tweet_text)
                 count += 1
             else:
                break

    except:
        print('There is no data saved yet')


def view_all_saved_reddit(user_choice):
    # viewing all the records
    search_session_reddit = Session()
    try:
         reddit = search_session_reddit.query(Reddit).all()
         row_count = search_session_reddit.query(Reddit).filter(Reddit.id > 0).count()
         count = 0
         while count != row_count:
             if user_choice == '1':
                 print('*', reddit[count].subreddit_title)
                 count += 1
             elif user_choice == '2':
                 print('*', reddit[count].url_subreddit)
                 count += 1

             elif user_choice == '3':
                 print('*', reddit[count].reddit_trending_news)
                 count += 1
             else:
                 break

    except:
        print('There is no data saved yet')


def view_all_saved_youtube(user_choice):
    # viewing all the records
    search_session_youtube = Session()
    try:
         youtube = search_session_youtube.query(Youtube).all()
         row_count = search_session_youtube.query(Youtube).filter(Youtube.id > 0).count()
         count = 0
         while count != row_count:
             if user_choice == '1':
                 print('*', youtube[count].video_names)
                 count += 1
             elif user_choice == '2':
                 print('*', youtube[count].channels)
                 count += 1

             elif user_choice == '3':
                 print('*', youtube[count].url_youtube)
                 count += 1
             else:
                break

    except:
        print('There is no data saved yet')
