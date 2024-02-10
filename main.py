SPRAVOCHNIK_FILE: str = 'spravochnik.txt'


def load_spravochnik() -> list[list[str]]:
    """
    Загружает данные справочника из файла и возвращает их в виде списка списков строк.
    Если файл пустой, выводит сообщение об этом.
    """
    spravochnik = []
    try:
        with open(SPRAVOCHNIK_FILE, 'r') as file:
            for line in file:
                entry = line.strip().split(';')
                spravochnik.append(entry)
    except IOError:
        print("Файл справочника пустой. Добавьте новую запись.")
    return spravochnik


def save_spravochnik(spravochnik: list[list[str]]) -> None:
    """
    Сохраняет данные справочника из списка списков строк в файл.
    """
    with open(SPRAVOCHNIK_FILE, 'w') as file:
        for entry in spravochnik:
            line = ';'.join(entry)
            file.write(line + '\n')


def display_page(page: int, page_size: int) -> None:
    """
    Выводит информацию из справочника постранично на основе номера страницы
    и размера страницы.
    """
    spravochnik = load_spravochnik()
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    page_data = spravochnik[start_index:end_index]
    for entry in page_data:
        print(f"Фамилия: {entry[0]}")
        print(f"Имя: {entry[1]}")
        print(f"Отчество: {entry[2]}")
        print(f"Организация: {entry[3]}")
        print(f"Рабочий телефон: {entry[4]}")
        print(f"Личный телефон: {entry[5]}")
        print()


def add_entry() -> None:
    """
    Добавляет новую запись в справочник на основе введенных пользователем
    данных.
    """
    spravochnik = load_spravochnik()
    entry = []
    entry.append(input("Введите фамилию: "))
    entry.append(input("Введите имя: "))
    entry.append(input("Введите отчество: "))
    entry.append(input("Введите название организации: "))
    entry.append(input("Введите рабочий телефон: "))
    entry.append(input("Введите личный телефон: "))
    spravochnik.append(entry)
    save_spravochnik(spravochnik)
    print("Запись успешно добавлена!")


def edit_entry() -> None:
    """
    Редактирует существующую запись в справочнике на основе введенных
    пользователем данных.
    """
    spravochnik = load_spravochnik()
    entry_index = int(input("Введите индекс записи, которую хотите "
                            "отредактировать: "))
    if entry_index < 0 or entry_index >= len(spravochnik):
        print("Неверный индекс записи!")
        return
    entry = spravochnik[entry_index]
    entry[0] = input("Введите фамилию: ")
    entry[1] = input("Введите имя: ")
    entry[2] = input("Введите отчество: ")
    entry[3] = input("Введите название организации: ")
    entry[4] = input("Введите рабочий телефон: ")
    entry[5] = input("Введите личный телефон: ")
    save_spravochnik(spravochnik)
    print("Запись успешно отредактирована!")


def main() -> None:
    """
    Основная функция программы для взаимодействия с пользователем.
    """
    while True:
        print("1. Вывод постранично записей из справочника")
        print("2. Добавление новой записи в справочник")
        print("3. Редактирование записей в справочнике")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            page = int(input("Введите номер страницы: "))
            page_size = int(input("Введите размер страницы: "))
            display_page(page, page_size)
        elif choice == '2':
            add_entry()
        elif choice == '3':
            edit_entry()
        elif choice == '0':
            break
        else:
            print("Неверный выбор!")


if __name__ == '__main__':
    main()
