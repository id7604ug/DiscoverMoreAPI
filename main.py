import user_interface
import api_requests

def handle_choice(user_choice):
    # function to handle the choice selected 
    if user_choice == '1':
        api_requests.get_tweets()

    elif user_choice == '2':
        print('do something')

    elif user_choice == '3':
        print('do something')

    elif user_choice == '4':
        print('do something')

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
