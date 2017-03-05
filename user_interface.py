def display_menu_twitter():
    #Displaying the menu choice
    print('''
              ***TWITTER MENU***

        1. Search Tweets on Twitter
        2. Update a status on Twitter
        3. Search users on Twitter
        4. Delete a status on Twitter
        5. Update a status on Twitter
        e. Exit to main menu
    ''')

    user_choice = input('Enter your selection: ')
    return user_choice

def display_menu_reddit():
    #Displaying the menu choice
    print('''
              ***REDDIT MENU***

        1. Search Subreddits on Reddit
        e. Exit to main menu
    ''')

    user_choice = input('Enter your selection: ')
    return user_choice

def display_menu_youtube():
    #Displaying the menu choice
    print('''
              ***YOUTUBE MENU***

        1. Search videos on Youtube
        e. Exit to main menu
    ''')

    user_choice = input('Enter your selection: ')
    return user_choice


def display_main_menu():
    #Displaying the menu choice
    print('''
        ***MAIN MENU***

        1. Twitter
        2. Reddit
        3. Youtube
        4. Search all Sites*NOT YET WORKING
        q. Quit
    ''')

    user_choice = input('Enter your selection: ')
    return user_choice


def get_user_search():
    #getting the user search
    user_input = input("Enter a search: ")
    print('')
    return user_input

def get_user_tweet_count():
  # while loop to make user is entering a number
    while True:
        try:
            # getting input for how many tweets the user wants returned
            user_input = int(input("Enter an amount of tweets you want to search (1-100): "))
            if user_input > 100:
                print('Please enter a number less than 100')
                pass
            else:
                break
        except ValueError:
            print('please enter a int')

    return user_input

def get_user_youtube_count():
  # while loop to make user is entering a number
    while True:
        try:
            # getting input for how many tweets the user wants returned
            user_input = int(input("Enter an amount of youtube videos you want to return (1-15): "))
            if user_input > 15:
                print('Please enter a number less than 15')
                pass
            else:
                break
        except ValueError:
            print('please enter a int')
    print('')
    return user_input
