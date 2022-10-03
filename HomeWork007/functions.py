import csv
import data_base
import logger
from HomeWork007.main import window


def add_info():
    logger.log_input_in_add_section()
    name = input('Name: ')
    id_phone = input('Phone: ')
    residence = input('Place of residence: ')
    logger.log_add_in_phonebook_record(name, id_phone, residence)
    new_line = (id_phone, name, residence)
    window.new_text.setText(" ".join(new_line))
    with open(data_base.path, 'a', newline='') as data:
        writer = csv.writer(data, delimiter=';')
        writer.writerow(new_line)


def find_num():
    logger.log_input_in_find_section()
    id_phone = input('Phone: ')
    logger.log_find_record_in_phonebook(id_phone)
    with open(data_base.path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if id_phone == row[0]:
                print('Phone: {:<15} Name: {:<15} From: {:<15}'.format(*row))


def show_all():
    logger.log_input_in_show_all_section()
    with open(data_base.path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print('Phone: {:<15} name: {:<15} From: {:<15}'.format(*row))


def delete_item():
    logger.log_input_in_delete_section()
    updated_list = []
    with open(data_base.path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        id_phone = input('write the Phone(id) you want to remove from the directory: ')
        for row in reader:
            if row[0] != id_phone:
                updated_list.append(row)
        update_file(updated_list)
        logger.log_delete_record(id_phone)


def update_file(updated_list):
    with open(data_base.path, "w", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(updated_list)
        print("File has been updated")
