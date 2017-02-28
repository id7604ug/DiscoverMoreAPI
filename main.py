import user_interface
import api_requests
from datastore import call_get_tweets


def handle_choice(user_choice):
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
    elif user_choice == 'q':
        quit()

    else:
       print('Please enter a valid selection')


def main():

    quit_program = 'q'
    user_choice = None

    while user_choice != quit_program:
        user_choice = user_interface.display_menu_get_choice()
        handle_choice(user_choice)


if __name__ == '__main__':
    main()
