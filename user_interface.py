def display_menu_get_choice():
    #Displaying the menu choice
    print('''
        1. Search Twitter
        2. Make this do something
        3. Make this do something
        4. Make this do something
        q. Quit
    ''')

    user_choice = input('Enter your selection: ')
    return user_choice

def get_user_search():
    #getting the user search
    user_input = input("Enter a search: ")
    return user_input

def get_user_tweet_count():
  # while loop to make sure user is entering a number
    while True:
        try:
            # getting in put for how many tweets the user wants returned
            user_input = int(input("Enter an amount of tweets you want to search (1-100): "))
            break
        except ValueError:
            print('please enter a int')

    return user_input
