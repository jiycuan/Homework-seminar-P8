def homework_t(id):

    with open("teachers.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        if id in line:
            line = line.split(', ')
            name = line[1]

    data_for_file_t = str(input('Укажите текст домашнего задания: '))
    with open("homework_t.txt","a", encoding='UTF-8') as file:
        file.write(f'\n{name}, {data_for_file_t} ')

def homework_s(id):

    with open("students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        if id in line:
            line = line.split(', ')
            name = line[1]

    data_for_file = str(input('Укажите через запятую ответы к домашним заданиям: '))
    with open("homework_s.txt","a", encoding='UTF-8') as file:
        file.write(f'\n{name}, {data_for_file}')