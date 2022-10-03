import logging
import data_base

logging.basicConfig(filename=data_base.path_log, filemode='a', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',)


def exit_log():
    logging.info('user logged out')


def input_log():
    logging.info('user is logged in')


def log_input_in_add_section():
    logging.info('add in phonebook record')


def log_add_in_phonebook_record(id_phone, name, residence):
    logging.info(f'add in phonebook: {id_phone} {name} {residence}')


def log_input_in_find_section():
    logging.info('find in phonebook record')


def log_find_record_in_phonebook(id_phone):
    logging.info(f'there was a search: {id_phone}')


def log_input_in_show_all_section():
    logging.info('show in phonebook all records')


def log_input_in_delete_section():
    logging.info('delete in phonebook record')


def log_delete_record(id_phone):
    logging.info(f'was removed: {id_phone}')
