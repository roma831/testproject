from csv import reader
from random import sample


YEARS = {2014, 2016, 2017}

def open_table():
    with open('books.csv', 'r') as csvfile:
        table = list(reader(csvfile, delimiter=';'))
        return table[1:]


def get_year(row):
    date = row[6].split()[0]
    return int(date.split('.')[2])


def get_author(row):
    return row[3] or 'Автор не указан'


def find_string(searchline, string):
    return string.lower().find(searchline.lower())


def count_long_titles(table):
    count = 0
    for row in table:
        if len(row[1]) > 30:
            count += 1
    print(f'Количество записей с названием длиннее 30 символов: {count}')


def search(table):
    searchline = input('Введите автора: ')
    count = 0
    for row in table:
        author_found = (find_string(searchline, row[3]) != -1)
        year = get_year(row)
        if author_found and year in YEARS:
            count += 1
            print(
                f'{count}. {get_author(row)}. '
                f'{row[1]} - {year}'
            )
    if count == 0:
        print('Ничего не найдено.')



def generate_references(table):
    selected = sample(table, 20)
    with open('bibliography.txt', 'w', encoding='utf-8') as output:
        for number, row in enumerate(selected, start=1):
            year = get_year(row)
            author = ' '.join(get_author(row).split())
            title = ' '.join(row[1].split())
            line = f'{number}. {author}. {title} - {year}'
            output.write(line + '\n')
    print('20 ссылок сохранены в bibliography.txt.')



table = open_table()
while True:
    print(
            '\nМеню:\n'
            '1 - Подсчитать названия длиннее 30 символов\n'
            '2 - Поиск по автору (только 2014, 2016 и 2017 годы)\n'
            '3 - Создать 20 библиографических ссылок\n'
            '0 - Выход'
        )
    menu = input('Выберите пункт меню: ')
    match menu:
        case '1':
            count_long_titles(table)
        case '2':
            search(table)
        case '3':
            generate_references(table)
        case '0':
            break
        case _:
            print('Нет такого пункта меню!')
    input('Нажмите Enter')