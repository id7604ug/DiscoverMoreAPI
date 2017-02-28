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
