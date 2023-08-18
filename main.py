import io


# Заполнение справочника телефонов
def add_records(file):
    contact = dict()
    contact['surname'] = input('Введите фамилию: ')
    contact['name'] = input('Введите имя: ')
    contact['second_name'] = input('Введите отчество: ')
    contact['organization'] = input('Введите название организации: ')
    contact['job_phone'] = input('Введите рабочий телефон: ')
    contact['mobile_phone'] = input('Введите сотовый телефон: ')

    # содержание файла
    data = '{surname},{name},{second_name},{organization},{job_phone},{mobile_phone}\n'

    # запись в файл
    with open(file, 'a') as f:
        f.write(data.format(**contact))


# Функция поиска записей в справочнике
def search_records(file):
    data = list()  # список с информацией из файла
    found = list()  # список с найдеными контактами
    criteria = input('Введите имя или другую информацию о контакте в полном объёме: ')
    # чтение содержимого файла
    with io.open(file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    # разбор строк и заполнение списка со значениями
    for line in lines:
        data.append(list(line.split(',')))
    # поиск по критерию
    for line in data:
        for value in line:
            if criteria in value:
                found.append(line)
                break
    # вывод найденых контактов
    for contact in found:
        print('{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}{5:<20}'.format(contact[0], contact[1], contact[2], contact[3],
                                                                  contact[4], contact[5]))


# Функция вывода постранично записей из справочника на экран
def show_records(page, records, contact=None):
    # вычисляем индексы начала и конца отображения текущей страницы
    start_index = page * page_size
    end_index = (page + 1) * page_size


    # выводим информацию о записях
    with open("PhoneBook.txt", "r") as file:
        for i in range(start_index, min(end_index, len(records))):
            date = records[i]
            print(i + 1, date)
           # print(file.read())




# Функция редактирования записей в справочнике
def edit_records(index, file):
    # проверяем, что индекс находится в пределах допустимых значений
    if index not in range(len(records_phonebook)):
        print("Такой записи нет")
        return

    record = records_phonebook[index]
    print("Редактируемая запись: {} {} {} {} {} {}".format(record[0], record[1], record[2],
                                                     record[3], record[4], record[5]))

    surname = input('Введите фамилию: ')
    name = input("Введите имя контакта: ")
    second_name = input('Введите отчество: ')
    organization = input('Введите название организации: ')
    job_phone = input('Введите рабочий телефон: ')
    mobile_phone = input('Введите сотовый телефон: ')

    record = (surname, name, second_name, organization, job_phone,mobile_phone)
    records_phonebook[index] = record
    phone_book = open('PhoneBook.txt', 'a')
    print(surname, name, second_name, organization, job_phone, mobile_phone)
    phone_book.close()


# Список записей в справочнике
records_phonebook = []
# Количество записей на страницу
page_size = 5


# Основной цикл программы
while True:
    action = input("Введите команду из предложенных: add, show, edit, find:")
    print()
    file_name = 'PhoneBook.txt'
    # Добавление новой записи в справочник
    if action == "add":
        add_records(file_name)
    # Вывод записей из справочника на экран
    elif action == "show":
        page = int(input("Введите, номер страницы начиная с '0': "))
        show_records(page, file_name)
    # Редактирование записей в справочнике
    elif action == "edit":
        index = int(input("Введите индекс записи:"))
        edit_records(index)
    # Поиск записей в справочнике
    elif action == "find":
        #print("\nНайдено записей: {}".format(len(found_records)))
        search_records(file_name)
    else:
        print("Неизвестная команда, повторите ввод!")