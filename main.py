import user_interface
import api_requests
from datastore import call_get_tweets


def handle_choice_twitter(user_choice):
    user_tweets = api_requests.UserApiRequest()
    # function to handle the choice selected
    if user_choice == '1':
        # searching tweets
        call_get_tweets()

    elif user_choice == '2':
        user_tweets.status_update()

    elif user_choice == '3':
        user_tweets.search_twitter_user()

    elif user_choice == '4':
        user_tweets.delete_status()

    elif user_choice == '5':
        user_tweets.status_update()

    elif user_choice == 'e':
        main()


    else:
       print('Please enter a valid selection')

def handle_choice_reddit(user_choice):
    user_reddit = api_requests.RedditAPIRequest()
    # function to handle the choice selected
    if user_choice == '1':
        user_reddit.search_reddit()

    elif user_choice == 'e':
        main()

    else:
       print('Please enter a valid selection')

def handle_choice_main(user_choice):
    # function to handle the choice selected
    if user_choice == '1':
        open_twitter()

    elif user_choice == '2':
        open_reddit()

    elif user_choice == '3':
        pass

    elif user_choice == '4':
        pass

    elif user_choice == 'q':
        quit()

    else:
       print('Please enter a valid selection')

def open_twitter():

    quit_twitter = 'e'
    choice = None

    while choice != quit_twitter:
        choice = user_interface.display_menu_twitter()
        handle_choice_twitter(choice)

def open_reddit():

    quit_reddit = 'e'
    choice = None

    while choice != quit_reddit:
        choice = user_interface.display_menu_reddit()
        handle_choice_reddit(choice)

def main():

    quit_program = 'q'
    user_choice = None

    while user_choice != quit_program:
        user_choice = user_interface.display_main_menu()
        handle_choice_main(user_choice)


if __name__ == '__main__':
    main()
