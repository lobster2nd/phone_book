import os.path


def request_valid(rec: str) -> bool:
    """Проверка валидности введённых данных. Все поля должны быть заполнены"""
    return rec.count(',') == 5


def print_records(file_name: str):
    """Вывод всех записей базы данных"""
    with open(file_name, encoding='UTF-8') as f:
        data = f.read()
        if not data:
            print('Список пустой. Добавьте первую запись.')
        print(data)


def search(rec: str, file_name: str) -> list:
    """Поиск записей по ключевым словам"""
    rec = [v.strip() for v in rec.split(', ')]
    with open(file_name, 'r', encoding='UTF-8') as f:
        matches = []
        matches = [data for data in f.readlines() if all(item in data for item in rec) and data not in matches]
        return matches if matches else ['Ничего не найдено']


def add_record(rec: str, file_name: str):
    """Добавление новой записи"""
    if search(rec, file_name)[0] == rec + '\n':
        print('Такая запись в базе данных уже есть')
    else:
        with open(file_name, 'a+', encoding='UTF-8') as f:
            f.write(rec + '\n')
            print('Запись успешно добавлена')


def edit_record(rec: list, file_name: str):
    """Редактирование записи"""
    print(f'Будет отредактирована запись: {rec}')
    new_rec = input('Введите новые данные:' + '\n')
    if request_valid(new_rec):
        with open(file_name, 'r', encoding='UTF-8') as f:
            old_data = f.read()
        new_data = old_data.replace(rec, new_rec)
        with open(file_name, 'w', encoding='UTF-8') as f:
            f.write(new_data)
            print('Запись успешно отредактирована')
    else:
        print('Проверьте правильность введенных данных')


file = input('Введите название файла с расширением: \n')
if not os.path.isfile(file):
    f = open(file, "x")
    f.close

action = input("""Что вы хотите сделать?
    1 - Вывести все записи на экран
    2 - Добавить новую запись
    3 - Редактировать существующую запись
    4 - Поиск записей по одной или нескольким характеристикам\n""")

if not action.isdigit() or int(action) not in range(1, 5):
    print('Пожалуйста, введите число от 1 до 4')

elif action == '1':
    print_records(file)
elif action == '2':
    person = input("""Введите данные через запятую в формате:
    фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)\n""")
    if request_valid(person):
        add_record(person, file)
    else:
        print('Проверьте правильность введенных данных')

elif action == '3':
    record = input('Какую запись хотите редактировать? Введите строку целиком или ключевые слова для поиска:\n')
    result = search(record, file)
    if result == ['Ничего не найдено']:
        print('Ничего не найдено')
    elif len(result) == 1:
        edit_record(record, file)
    else:
        for i in range(len(result)):
            print(i + 1, result[i].rstrip('\n'))
        usr_choice = int(input('Какую запись хотите отредактировать? Введите номер:\n'))
        edit_record(result[usr_choice - 1], file)


elif action == '4':
    words = input('Введите ключевые слова для поиска: \n').strip()
    result = (search(words, file))
    for i in result:
        print(i.rstrip('\n'))
