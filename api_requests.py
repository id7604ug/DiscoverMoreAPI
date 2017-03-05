import sys
from TwitterSearch import *
import data_base_tables
import user_interface
import tweepy

import praw

from bs4 import BeautifulSoup
import requests


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser



class UserApiRequest(object):
    def __init__(self):
        self.consumer_key ='5BWWX2DfMOJpWzw2WbQofKzeQ' # Please enter your consumer key here
        self.consumer_secret='IJnVpVqxyQxKQZ2JzLBFJ7s3pSmoyFxts4VLipMxkIsAzHtYWC' # Please enter your consumer secret here
        self.access_token='1508067367-1FzmtXFSJc0p8WpP0deZszljlzyLkryBAMPwqvQ' # Please enter your access token here
        self.access_token_secret='3nywRI2ZcKKvxSG3hCcRPACMMFULbdGJ9hT0s96YgSo1J' # Please enter your access token secret here
        self.screen_name = []
        self.date_tweet = []
        self.tweet_list = []
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    def get_tweets(self):
        self.screen_name = [] # setting the lists back to empty
        self.date_tweet = []
        self.tweet_list = []
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
    def __init__(self):

        self.client_id=''
        self.client_secret=''
        self.password=''
        self.user_agent=''
        self.username=''

        self.title = []
        self.urls = []


    def search_reddit(self):
        self.title = [] # setting the lists back to empty
        self.urls = []
        try:

            r = praw.Reddit(self.client_id,
                self.client_secret,
                self.password,
                self.user_agent,
                self.username)
            user_input = user_interface.get_user_search()
            user_input = user_input.replace(' ', '')
            for submission in r.subreddit(user_input).top(limit=5):
                print(submission.title)
                print(submission.url)

            r = praw.Reddit(client_id='', # enter your client ID
                client_secret='',          # enter your client secret
                password='',                # enter your account password
                user_agent='',              # enter your user agent
                username='')                # enter your account username
            user_input = user_interface.get_user_search()       # getting the user search
            user_input = user_input.replace(' ', '')        # getting rid of any spaces in the search
            for submission in r.subreddit(user_input).top(limit=5): # printing 5 subreddits
                print("Title:\n*",submission.title, '\n')
                self.title.append(submission.title)
                print("URL:\n*",submission.url, '\n')
                self.urls.append(submission.url)

            print('*** Hold Command and double click to activate URL link ***', '\n')


        except:
                e = sys.exc_info()[0]
                print('No results found')


    def display_reddit_trending_topic_now(self):
        trends = requests.get('https://www.reddit.com/r/Trending/')
        contents = BeautifulSoup(trends.content)
        current_trends = contents.find_all("div", {"class": "entry unvoted"})
        for child in current_trends:
            tagp = child.find_all('p', {'class': 'title'})
            for text in tagp:
                href_link = text.find('a')
                print(href_link.get('href'))
                for atext in text:
                    if atext.string is not None:
                        print(atext.string)
                    else:
                        pass



class YoutubeAPIRequest(object):
    def __init__(self):
        self.DEVELOPER_KEY = ''   # Enter your API key here
        self.YOUTUBE_API_SERVICE_NAME = 'youtube'
        self.YOUTUBE_API_VERSION = 'v3' # if using a different version enter it here
        self.video_names = []
        self.video_descriptions = []
        self.channels = []
        self.urls = []

    def search_youtube(self):
         self.video_names = [] # setting the lists back to empty
         self.video_descriptions = []
         self.channels = []
         self.urls = []

         try:

          user_input = user_interface.get_user_search() # getting the user search
          user_count = user_interface.get_user_youtube_count() # getting the user count for search results
          argparser.add_argument("--q", help="Search term", default=user_input)  # adding arguments
          argparser.add_argument("--max-results", help="Max results", default=user_count)
          options = argparser.parse_args()

          youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,  # building the the youtube object
            developerKey=self.DEVELOPER_KEY)

          search_response = youtube.search().list(  # getting the search parameters
            q=options.q,
            part='snippet,id',
            type='video',
            maxResults=options.max_results
          ).execute()

          for search_result in search_response.get('items', []):
            self.video_names.append('%s' % (search_result['snippet']['title'])) # adding the title
            self.video_descriptions.append('%s' % (search_result["snippet"]["description"])) # adding the description
            self.channels.append('%s' % (search_result["snippet"]["channelTitle"])) # adding the name of the channel
            video_id = (search_result['id']["videoId"]) # getting the video ID
            self.urls.append('%s' % ('https://www.youtube.com/watch?v=' + video_id)) # adding the video id to the rest of the URL

          count = 0
          while count != len(self.video_descriptions): # printing each element of the lists
            print ("Video Name:\n*", self.video_names[count], "\n")
            print("Video Description:\n*", self.video_descriptions[count], "\n")
            print("Channel:\n*", self.channels[count], "\n")
            print ("URL:\n*", self.urls[count], "\n")
            count += 1

            print('*** Hold Command and double click to activate URL link ***', '\n')

         except HttpError as e:
             print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)) # catching errors

