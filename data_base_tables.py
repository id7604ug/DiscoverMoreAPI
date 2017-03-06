from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Create engine.
engine = create_engine('sqlite:///discover_more.db', echo=True)
Base = declarative_base()

class Twitter(Base):

   # creating a table
    __tablename__ = 'twitter'

    # creating the columns
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    tweet_text = Column(String)
    tweet_date = Column(String)


    def __init__(self, user_name, tweet_text, tweet_date):
        self.user_name = user_name
        self.tweet_text = tweet_text
        self.tweet_date = tweet_date


    def __repr__(self):
        return 'twitter: id = {} user_name = {} tweet_text = {} tweet_date = {} '.format(self.id, self.user_name, self.tweet_text, self.tweet_date)

class Reddit(Base):

   # creating a table
    __tablename__ = 'reddit'

    # creating the columns
    id = Column(Integer, primary_key=True)
    subreddit_title = Column(String)
    url_subreddit = Column(String)
    reddit_trending_news = Column(String)


    def __init__(self, subreddit_title, url_subreddit):
        self.subreddit_title = subreddit_title
        self.url_subreddit = url_subreddit





    def __repr__(self):
        return 'reddit: id = {} subreddit_title = {} url_subreddit = {} '.format(self.id, self.subreddit_title, self.url_subreddit)

class Youtube(Base):

   # creating a table
    __tablename__ = 'youtube'

    # creating the columns
    id = Column(Integer, primary_key=True)
    video_names = Column(String)
    channels = Column(String)
    url_youtube = Column(String)


    def __init__(self, video_names, channels, url_youtube):
        self.video_names = video_names
        self.channels = channels
        self.url_youtube = url_youtube


    def __repr__(self):
        return 'youtube: id = {} video_names = {} channels = {} url_youtube = {} '.format(self.id, self.video_names, self.channels, self.url_youtube)


class RedditTrending(Base):
    __tablename__ = 'trending'
    id = Column(Integer, primary_key=True)
    reddit_trending_news = Column(String)
    reddit_treding_link = Column(String)

    def __init__(self, reddit_trending_news):
        self.reddit_trending_news = reddit_trending_news


    def __str__(self):
        return 'Trending: id={} reddit_trending_news={} reddit_trending_link={}'.format(self.id, self.reddit_trending_news)


