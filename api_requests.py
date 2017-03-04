import sys
from TwitterSearch import *
import data_base_tables
import user_interface
import tweepy
import praw


class UserApiRequest(object):
    def __init__(self):
        self.consumer_key ='' # Please enter your consumer key here
        self.consumer_secret='' # Please enter your consumer secret here
        self.access_token='' # Please enter your access token here
        self.access_token_secret='' # Please enter your access token secret here
        self.screen_name = []
        self.date_tweet = []
        self.tweet_list = []
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

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
                # adding the tweets to lists to add to the database
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

    # Update a status on Twitter
    def status_update(self):
        """This method updates a user status on twitter using the text enter by the user"""
        status_post = input("Please enter status: ")
        self.api.update_status(status=status_post, lat=45.0123061, long=-93.2358652)
        print('Status message: {} successfully updated to your twitter account'.format(status_post))

    # Delete a status on Twitter
    def delete_status(self):
        """This method deletes a user status on Twitter. Only the first 5 tweets are
         display. You can increase count parameter to display specified number of tweets"""
        user_time_line = self.api.user_timeline(count=5)
        print('Enter 0 to exit deleting statuses')
        for i in range(len(user_time_line)):
            print('Enter {} to delete tweet: {}'.format(i+1, user_time_line[i].text))
        while True:
            try:
                delete_tweet = int(input("Enter your choice for the tweet you want deleted: "))
                if delete_tweet == 0:
                    break
                print(user_time_line[delete_tweet-1].text + 'successfully deleted')
                self.api.destroy_status(user_time_line[delete_tweet-1].id)
            except ValueError:
                print('Please enter a valid number!!! Input error')
                continue

    # Search a user on twitter
    def search_twitter_user(self):
        """This method search Twitter for a valid user. Return result is 5.
         You can increase count variable to specified the amount of result to display"""
        name = input("Please enter a Twitter user name would like to search: ")
        twitter_user_name = self.api.search_users(q=name, count=10)
        for user in twitter_user_name:
            print('User name: {}, User screen name: {}, User location: {}, User description: {}'\
                  .format(user.name, user.screen_name, user.location, user.description))


class RedditAPIRequest(object):

    def search_reddit(self):
        try:
            r = praw.Reddit(client_id='',
                client_secret='',
                password='',
                user_agent='',
                username='')
            user_input = user_interface.get_user_search()
            user_input = user_input.replace(' ', '')
            for submission in r.subreddit(user_input).top(limit=5):
                print(submission.title)
                print(submission.url)

        except:
                e = sys.exc_info()[0]
                print('No results found')
