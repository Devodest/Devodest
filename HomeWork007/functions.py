import csv
import data_base




def add_info():
    name = input('Name: ')
    id = input('Phone: ')
    From = input('Place of residence: ')
    new_line = (id, name, From)
    with open(data_base.path, 'a', newline='') as data:
        writer = csv.writer(data, delimiter=';')
        writer.writerow(new_line)


def find_num():
    id = input('Phone: ')
    with open(data_base.path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if id == row[0]:
                print('Phone: {:<15} Name: {:<15} From: {:<15}'. format(*row))


def show_all():
    with open(data_base.path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print('Phone: {:<15} name: {:<15} From: {:<15}'. format(*row))


def delete_item():
    updatedlist = []
    with open(data_base.path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        id = input('write the Phone(id) you want to remove from the directory: ')
        for row in reader:
            if row[0] != id:
                updatedlist.append(row)
        updatefile(updatedlist)


def updatefile(updatedlist):
    with open(data_base.path, "w", newline='') as f:
        Writer = csv.writer(f, delimiter=';')
        Writer.writerows(updatedlist)
        print("File has been updated")


# def data_add():


# def data_delete()