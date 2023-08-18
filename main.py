def request_valid(record: str) -> bool:
    """Проверка валидности введённых данных. Все поля должны быть заполнены"""
    return record.count(',') == 5


def file_exists(file: str) -> bool:
    """Проверка существования файла базы данных"""
    try:
        f = open(file)
        f.close()
    except IOError:
        return False
    return True


def print_records(file_name: str):
    """Вывод всех записей базы данных"""
    with open(file_name, encoding='UTF-8') as f:
        for pers in f.readlines():
            print(pers.rstrip('\n'))


def search(value: str, file_name: str) -> str:
    """Поиск записей по ключевым словам"""
    value = [v.strip() for v in value.split(',')]
    with open(file_name, encoding='UTF-8') as f:
        matches = []
        for data in f.readlines():
            for item in value:
                if item in data and data not in matches:
                    matches.append(data)
        return matches if matches else 'Ничего не найдено'


def add_record(record: str, file_name: str):
    with open(file_name, 'a+', encoding='UTF-8') as f:
        f.write(record + '\n')
        print('Запись успешно добавлена')


file = input('Введите название файла с расширением: \n')
action = input("""Что вы хотите сделать?
    1 - Вывести все записи на экран
    2 - Добавить новую запись
    3 - Редактировать существующую запись
    4 - Поиск записей по одной или нескольким характеристикам\n""")

if not action.isdigit() or int(action) not in range(1, 5):
    print('Пожалуйста, введите число от 1 до 4')

elif action == '1':
    if file_exists(file):
        print_records(file)
    else:
        print('Файл базы данных ещё не создан. Добавьте первую запись.')

elif action == '2':
    person = input("""Введите данные через запятую в формате:
    фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)\n""")
    if request_valid(person):
        add_record(person, file)
    else:
        print('Проверьте правильность введенных данных')

elif action == '4':
    words = input('Введите ключевые слова для поиска: \n').strip()
    if request_valid(words):
        print(*search(words, file))
    else:
        print('введите данные в правильном формате')