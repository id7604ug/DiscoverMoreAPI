from TwitterSearch import *
import user_interface


class UserApiRequest(object):
    def __init__(self):
        self.consumer_key = '' # Please enter your consumer key here
        self.consumer_secret='' # Please enter your consumer secret here
        self.access_token=''# Please enter your access token here
        self. access_token_secret='' # Please enter your access token secret here

    def get_tweets(self):
        try:
            user_search = user_interface.get_user_search() # getting the suer search
            get_tweet_count = user_interface.get_user_tweet_count() # getting the amount of tweets
            tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
            tso.set_keywords([user_search])  # settiing the keyword
            tso.set_language('en')  # setting it to English only
            tso.set_include_entities(False)  # not including entities

            ts = TwitterSearch(
                self.consumer_key,
                self.consumer_secret,
                self.access_token,
                self.access_token_secret
            )

            test = 0
            for tweet in ts.search_tweets_iterable(tso):
                # print out to display tweets
                print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
                test += 1
                # will stop displaying tweets per user request
                if test == get_tweet_count:
                    break

        except TwitterSearchException as e:  # catch any errors
            print(e)

    # Search a user on twitter method
    def search_twitter_user(self):
        pass
