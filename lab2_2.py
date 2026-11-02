from csv import reader


def open_table():
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = list(reader(csvfile, delimiter=';'))
    return table[1:]


def show_publishers(table):
    publishers = set()
    for row in table:
        publishers.add(row[4])
    print('Перечень издательств:')
    for publisher in publishers:
        print(publisher)


def get_downloads(row):
    return int(row[5])


def popular_books(table):
    popular = sorted(table, key=get_downloads, reverse=True)
    print('\n20 самых популярных книг:')
    for number, row in enumerate(popular[:20], start=1):
        print(f'{number}. {row[1]} ')


table = open_table()
show_publishers(table)
popular_books(table)


