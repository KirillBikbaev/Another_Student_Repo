import csv


def write_data_in_Data(filename):

    with open(filename, 'w') as file:

        file.write(','.join(titles)) # объединение кортежа заголовков в строку через ','

        for line in data:
            line = [str(i) for i in line]
            line = ','.join(line)
            file.write(line) # объединение кортежей данных в строки через ','
        file.write('\n')

def insert(line):
    if line not in data:
        data.append(line)

def new_line_in_data():

    new_line = tuple(input('Введите данные: ').split())

    if new_line not in data:
        data.append(new_line)

def read_from_Data(filename):

    with open(filename, 'r') as file:

        titles = tuple(file.readline().split(','))
        data = []

        for line in file:
            line = tuple(line.split(','))
            data.append(line)

    return titles, data

global data, titles

titles = ('User_Number', 'Nickname')
data = []

titles, data = read_from_Data('New_Data_Base.csv')

new_line_in_data()

write_data_in_Data('New_Data_Base.csv')

print(data)