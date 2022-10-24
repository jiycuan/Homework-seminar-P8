from modules.read_data import read_data_s
from modules.read_data import read_data_t
from modules.read_data import read_data_sf
from modules.homework import homework_t
from modules.homework import homework_s

def ui(): # Сначала назвал verify_id, но потом осознал, что этот метод каскадом запускает все остальные составляющие интерфейса. И переименовал. 
    id = input("Укажите ID. Если указать несуществующий ID - база не выдаст никаких данных, хотя и притворится, что работает: ")
    # У всех записанных в базу людей к цифровому идентификатору приписан буквенный для определения их роли. 
    teacher = 'IMTS' # IMTS расшифровывается как "I'm a teacher, I swear"
    student = 'SH' # SH расшифровывается как "So hungry"
    
    if teacher in id:
        teacher_mode_ui(id)
    if student in id:
        student_mode_ui(id)
    else:
        temp = int(input("Если нужно посмотреть данные по другому ID - нажмите 1. Если выйти из программы - 0. "))
        if temp == 1:
            ui()

def verify():
    number = int(input("Укажите цифрой номер пункта меню: "))
    if number in [1, 2, 3, 4, 5]:
        return number
    else:
        print("Неверный ввод, повторите попытку")
        verify()

def teacher_mode_ui(id):
    print("Учителям доступны следующие действия:")
    print("1: Что я преподаю?")
    print("2: Когда я смогу поспать?")
    print("3: Выдать новые домашние задания")
    print("4: А список студентов есть?")
    print("5: Выход")

    while True:
        print("")
        dowhat = verify()

        if dowhat == 1:
            read_data_t(id)

        if dowhat == 2:
            print("Когда сделаешь всю работу. И ни секундой раньше.")

        if dowhat == 3:
            homework_t(id)

        if dowhat == 4:
            read_data_s()

        if dowhat == 5:
            print("До свидания! Можешь идти вытирать кровавые слёзы")
            break

def student_mode_ui(id):
    print("Студентам доступны следующие действия:")
    print("1: Сегодня учимся?")
    print("2: А когда обед?")
    print("3. Сдать домашнее задание") 
    print("4: А кто учится на моём факультете?")
    print("5: Выход")

    while True:
        print("")
        dowhat = verify()

        if dowhat == 1:
            print("Да, учимся. Даже если выходной. Даже если праздник. И на новый год тоже. Или ты будешь учиться, или... в общем, у тебя и выбора-то нет")

        if dowhat == 2:
            print("В 14:00, как обычно")

        if dowhat == 3:
            homework_s(id)

        if dowhat == 4:
            read_data_sf(id)

        if dowhat == 5:
            print("До свидания! И помни - однажды ты выйдешь на работу.")
            break