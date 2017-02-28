def display_menu_get_choice():
    #Displaying the menu choice
    print('''
        1. Search Twitter
        2. Update a status on Twitter
        3. Search users on Twitter
        4. Delete a status on Twitter
        5. Update a status on Twitter
        q. Quit
    ''')

    user_choice = input('Enter your selection: ')
    return user_choice

def get_user_search():
    #getting the user search
    user_input = input("Enter a search: ")
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
