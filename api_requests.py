from TwitterSearch import *
import user_interface


def get_tweets():
    try:
        user_search = user_interface.get_user_search() # getting the suer search
        get_tweet_count = user_interface.get_user_tweet_count() # getting the amount of tweets
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_keywords([user_search])  # settiing the keyword
        tso.set_language('en')  # setting it to English only
        tso.set_include_entities(False)  # not including entities

        ts = TwitterSearch(
            consumer_key='CONSUMER_KEY', # Please enter your consumer key here
            consumer_secret='CONSUMER_KEY', # Please enter your consumer secret here
            access_token='ACCESS_TOKEN', # Please enter your access token here
            access_token_secret='ACCESS_TOKEN_SECRET' # Please enter your access token secret here
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
