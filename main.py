import os


# Функция добавления новой записи в телефонный справочник
def add_entry():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    org_name = input("Введите название организации: ")
    work_phone = input("Введите телефон рабочий: ")
    pers_phone = input("Введите телефон личный: ")

    # Запись данных в файл
    data_file = open('PhoneBook.txt', 'a')
    data_file.write('{};{};{};{};{};{};\n'.format(last_name, first_name, second_name, org_name, work_phone, pers_phone))


# Функция поиска записи в телефонном справочнике
def search_entry():
    search_key = input("Введите строку для поиска: ")
    search_results = ""

    # Поиск записи по указанной строке
    data_file.seek(0) # перемещение в начало файла
    for line in data_file:
        if search_key in line:
            search_results += line
    if search_results:
        print(search_results)
    else:
        print("По запросу '{}' записей не найдено".format(search_key))


# Функция редактирования записи в телефонном справочнике
def edit_entry():
    search_key = input("Введите ячейку строки: ")
    search_results = ""
    edit_data = []

    data_file.seek(0) # перемещение в начало файла
    for line in data_file:
        if search_key in line:
            search_results += line
            edit_data = line.split(';') # разделение строки на составляющие
    if search_results:
        # Запрос на редактирование соответствующих характеристик
        edit_data[0] = input("Введите фамилию [{}]: ".format(edit_data[0])) or edit_data[0]
        edit_data[1] = input("Введите имя [{}]: ".format(edit_data[1])) or edit_data[1]
        edit_data[2] = input("Введите отчество [{}]: ".format(edit_data[2])) or edit_data[2]
        edit_data[3] = input("Введите название организации [{}]: ".format(edit_data[3])) or edit_data[3]
        edit_data[4] = input("Введите телефон рабочий [{}]: ".format(edit_data[4])) or edit_data[4]
        edit_data[5] = input("Введите телефон личный [{}]: ".format(edit_data[5])) or edit_data[5]
    else:
        print("По запросу '{}' записей не найдено".format(search_key))

    # Запись отредактированных данных в файл
    if edit_data:
        with open('PhoneBook.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(search_results, '{};{};{};{};{};{}\n'.format(edit_data[0], edit_data[1],
                                                                                 edit_data[2], edit_data[3],
                                                                                 edit_data[4], edit_data[5]))

        with open('PhoneBook.txt', 'w') as f:
            f.write(new_data)


# Функция отображения телефонного справочника по страницам
def show_entry():
    count = 0
    # Отображение данных из файла
    data_file.seek(0)
    for line in data_file:
        count += 1
        if count > 9:
            count = 0
            print(line, end="")
            x = input("n - далее, q - выход: ")
            if x == 'q':
                break
        else:
            print(line, end="")


if __name__ == "__main__":
    # Открытие файла на чтение/запись
    if os.path.exists('PhoneBook.txt'):
        data_file = open('PhoneBook.txt', 'r')
    else:
        data_file = open('PhoneBook.txt', 'w')

    while True:
        # Вывод меню на экран
        print('''
Телефонный справочник:
1. Вывод постранично записей из справочника на экран
2. Добавление новой записи в справочник
3. Возможность редактирования записей в справочнике
4. Поиск записей по одной или нескольким характеристикам
5. Выход
        ''')
        # Выбор пункта меню
        x = int(input('Выберите пункт меню: '))
        if x == 1:
            show_entry()
        elif x == 2:
            add_entry()
        elif x == 3:
            edit_entry()
        elif x == 4:
            search_entry()
        elif x == 5:
            break
        else:
            print('Неверный пункт меню')

# Закрытие файла
data_file.close()