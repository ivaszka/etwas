"""Создать класс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена,
Тип переплета. Функции-члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов. Вывести:
a) список книг заданного автора;
b) список книг, выпущенных после заданного года."""
from random import randint

# проверка на пустое значение, пробел, табуляцию
def space(a):
    while a.isspace() or a == '':
        a = input('You enter nothing. Please enter something \n')
    return a

# проверка на корректность ввода года: только цифры и не старше 2020
def check_year(year):
    while not year.isdigit() or int(year) > 2020:
        year = input('It is not a year, enter a correct year less than 2020 \n')
    return int(year)

# проверка на корректность ввода количества: только строка с цифрами
def check_number(number):
    while not number.isdigit():
        number = input('It is not a number, enter a correct one \n')
    return number

# проверка на корректность ввода цены: только строка с цифрами по маске xx либо xx.xx
def check_cost(cost):
    cost_test = cost.replace('.', '', 1)
    while not cost_test.isdigit():
        cost = input('It is not a number. Enter a correct one by dot \n')
        cost_test = cost.replace('.', '', 1)
    return float(cost)


class Book:

    def __init__(self):
        self.title = space(input('Enter title \n'))
        self.author = space(input('Enter author \n'))
        self.year = check_year(input('Enter year \n'))
        self.cost = check_cost(input('Enter cost \n'))
        self.id = randint(100, 200)

    def write_book(self):
        new_book = [self.id, self.title, self.author, self.year, self.cost]
        print('Your book data:', new_book)


# запрос количества объектов класса книга
n = check_number(input('How many books do you have to make a list? \n'))
n = int(n)
# заполнение объектов класса
book_list = []
for i in range(n):
    book = Book()
    book_list.append(book)
for book in book_list:
    book.write_book()
# вывод книг по заданному автору
author = (input('Author? \n')).lower()
count = 0
for book in book_list:
    if author == (book.author).lower():
        print(book.title, ' by ', book.author)
        count += 1
if count == 0:
    print('There are no books by ', author, '\n')
#вывод книг автора по году издания старше заданного
year = check_year(input('Enter any year \n'))
year = int(year)
count = 0
for book in book_list:
    if year < book.year:
        print(book.title, ' by ', book.author, ' ,year:', book.year)
        count += 1
if count == 0:
    print('There are no books printed after', year, '\n')
