import user_input
import functions
import logger
from HomeWork007.main import window


def examination_choice():
    logger.input_log()
    while True:
        user_choice = user_input.menu()
        if user_choice == 'exit':
            window.new_text.setText('You are out of the directory ')
            print('You are out of the directory ')
            logger.exit_log()
            break
        else:
            window.new_text.setText(user_choice)
            if user_choice == '1':
                functions.add_info()
            elif user_choice == '2':
                functions.delete_item()
            elif user_choice == '3':
                functions.find_num()
            elif user_choice == '4':
                functions.show_all()
