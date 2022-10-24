def read_data_s():

    with open("students.txt","r", encoding='UTF-8') as file:
        data = file.read()
    print(data)

def read_data_t(id):

    with open("teachers.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        if id in line:
            line = line.split(', ')
            print(line[2])

def read_data_sf(id):

    with open("students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        if id in line:
            temp = line.split(', ')
            facultet = temp[2]
    
    with open("students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        if facultet in line:
            line = line.split(', ')
            print(line[1])