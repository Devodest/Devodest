import csv

path = r'data.csv'


def add_info():
    name = input('Name: ')
    phone = input('Phone: ')
    new_line = (name, phone)
    with open(path, 'a', newline='') as data:
        writer = csv.writer(data, delimiter=';')
        writer.writerow(new_line)


def find_num():
    name = input('Name: ')
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if name == row[0]:
                print(*row)


def show_all():
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            # print('Name: {:<15} Phone: {:<15}'. format(*row))
            print(row)


def delete_item():
    updatedlist = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        name = input('write the name you want to remove from the directory: ')
        for row in reader:
            if row[0] != name:
                updatedlist.append(row)
        updatefile(updatedlist)


def updatefile(updatedlist):
    with open(path, "w", newline='') as f:
        Writer = csv.writer(f, delimiter=';')
        Writer.writerows(updatedlist)
        print("File has been updated")
