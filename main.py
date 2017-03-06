import user_interface
import api_requests
from datastore import call_get_tweets, call_get_reddit, call_get_youtube, save_twitter_user_activity, display_user_tweets


def handle_choice_twitter(user_choice):
    user_tweets = api_requests.UserApiRequest()
    # function to handle the choice selected
    if user_choice == '1':
        # function to search tweets
        call_get_tweets()

    elif user_choice == '2':
        # function to change status update
        user_tweets.status_update()


    elif user_choice == '3':
        # function to search twitter users
        user_tweets.search_twitter_user()

    elif user_choice == '4':
        # function to delete status
        user_tweets.delete_status()

    elif user_choice == 'e':
        main()


    else:
       print('Please enter a valid selection')

def handle_choice_reddit(user_choice):
    user_reddit = api_requests.RedditAPIRequest()
    # function to handle the choice selected
    if user_choice == '1':
        # function to call the search Reddit
        call_get_reddit()

    elif user_choice == '2':
        user_reddit.display_reddit_trending_news()

    elif user_choice == 'e':
        main()

    else:
       print('Please enter a valid selection')

def handle_choice_youtube(user_choice):
    user_youtube = api_requests.YoutubeAPIRequest()
    # function to handle the choice selected
    if user_choice == '1':
        # function to call the search for Youtube
        call_get_youtube()



    elif user_choice == 'e':
        main()

    else:
       print('Please enter a valid selection')

# function to handle the choice selected
def handle_choice_main(user_choice):
    # Twitter
    if user_choice == '1':
        # opening the twitter menu
        open_twitter()

    # Reddit
    elif user_choice == '2':
        # opening the reddit menu
        open_reddit()

    # YouTube
    elif user_choice == '3':
        # opening the youtube menu
        open_youtube()

    # Search all
    elif user_choice == '4':
        pass

    elif user_choice == 'q':
        quit()

    else:
       print('Please enter a valid selection')

def open_twitter():
    # a function to open the twtter menu
    quit_twitter = 'e'
    choice = None

    while choice != quit_twitter:
        choice = user_interface.display_menu_twitter()
        handle_choice_twitter(choice)

def open_reddit():
    # a function to open the Reddit menu
    quit_reddit = 'e'
    choice = None

    while choice != quit_reddit:
        choice = user_interface.display_menu_reddit()
        handle_choice_reddit(choice)

def open_youtube():
    # a function to open the Youtube menu
    quit_youtube = 'e'
    choice = None

    while choice != quit_youtube:
        choice = user_interface.display_menu_youtube()
        handle_choice_youtube(choice)

def main():

    quit_program = 'q'
    user_choice = None

    while user_choice != quit_program:
        user_choice = user_interface.display_main_menu()
        handle_choice_main(user_choice)


if __name__ == '__main__':
    main()
