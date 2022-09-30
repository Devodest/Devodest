import user_input
import functions
def start():
    while True:
        user_choice = user_input.menu()
        if user_choice == 'exit':
            print('You are out of the directory ')
            break
        else:
            if user_choice == '1':
                functions.add_info()
            elif user_choice == '2':
                functions.delete_item()
            elif user_choice == '3':
                functions.find_num()
            elif user_choice == '4':
                functions.show_all()

