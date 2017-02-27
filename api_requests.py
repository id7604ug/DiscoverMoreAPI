from TwitterSearch import *
import data_base_tables
import user_interface


class UserApiRequest(object):
    def __init__(self):
        self.consumer_key = '' # Please enter your consumer key here
        self.consumer_secret='' # Please enter your consumer secret here
        self.access_token=''# Please enter your access token here
        self.access_token_secret='' # Please enter your access token secret here
        self.screen_name = []
        self.date_tweet = []
        self.tweet_list = []

    def get_tweets(self):
        try:
            user_search = user_interface.get_user_search() # getting the user search
            get_tweet_count = user_interface.get_user_tweet_count() # getting the amount of tweets
            print()
            tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
            tso.set_keywords([user_search])  # setting the keyword
            tso.set_language('en')  # setting it to English only
            tso.set_include_entities(False)  # not including entities

            ts = TwitterSearch(
                self.consumer_key,
                self.consumer_secret,
                self.access_token,
                self.access_token_secret
            )

            counter = 0
            for tweet in ts.search_tweets_iterable(tso):
                #adding the tweets to lists to add to the database
                self.screen_name.append(tweet['user']['screen_name'])
                self.tweet_list.append(tweet['text'])
                self.date_tweet.append(tweet['created_at'])
                # print out to display tweets
                print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']), '\n')
                counter += 1
                # will stop displaying tweets per user request
                if counter == get_tweet_count:
                    break

        except TwitterSearchException as e:  # catch any errors
            print(e)

    # Search a user on twitter method
    def search_twitter_user(self):
        pass
