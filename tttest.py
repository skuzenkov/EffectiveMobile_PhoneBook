# Заполнение справочника телефонов
def add_records():
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    address = input("Введите адрес контакта: ")
    email = input("Введите email контакта: ")
    record = (name, number, address, email)
    records_phonebook.append(record)


# Функция поиска записей в справочнике по одной или нескольким характеристикам
def search_records(search_values):
    # разделяем поисковый запрос на отдельные значения
    search_params = search_values.split(" ")

    # ищем совпадения с характеристиками в справочнике
    found_records = []
    for record in records_phonebook:
        for param in search_params:
            if param in record:
                found_records.append(record)
                break

    return found_records


# Функция вывода постранично записей из справочника на экран
def show_records(records, page):
    # вычисляем индексы начала и конца отображения текущей страницы
    start_index = page * page_size
    end_index = (page + 1) * page_size

    # выводим информацию о записях
    for i in range(start_index, min(end_index, len(records))):
        name, number, address, email = records[i]
        print("{}. {} {} {} {}".format(i + 1, name, number, addres, email))


# Функция редактирования записей в справочнике
def edit_records(index):
    # проверяем, что индекс находится в пределах допустимых значений
    if index not in range(len(records_phonebook)):
        print("Такой записи нет")
        return

    record = records_phonebook[index]
    print("Редактируемая запись: {} {} {} {}".format(record[0], record[1],
                                                     record[2], record[3]))

    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    address = input("Введите адрес контакта: ")
    email = input("Введите email контакта: ")

    record = (name, number, address, email)
    records_phonebook[index] = record


# Список записей в справочнике
records_phonebook = []
# Количество записей на страницу
page_size = 5

# Основной цикл программы
while True:
    action = input("Введите команду (? для помощи):")
    print()

    # Добавление новой записи в справочник
    if action == "add":
        add_records()
    # Вывод записей из справочника на экран
    elif action == "show":
        page = int(input("Введите, с какой страницы начать: "))
        show_records(records_phonebook, page)
    # Редактирование записей в справочнике
    elif action == "edit":
        index = int(input("Введите индекс записи:"))
        edit_records(index)
    # Поиск записей в справочнике
    elif action == "find":
        value = input("Введите характеристику или часть имени для поиска: ")
        found_records = search_records(value)
        print("\nНайдено записей: {}".format(len(found_records)))
        show_records(found_records, 0)

    else:
        print("Неизвестная команда")