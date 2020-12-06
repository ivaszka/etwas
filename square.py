"""Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
пользователем сторонами a и b на квадраты с наибольшей возможной на
каждом этапе стороной. Выведите длины ребер получаемых квадратов и кол-
во полученных квадратов."""
from random import randint


def square(a, b, array):
    if a == b:
        array.append(a)
        return array
    elif a < b:
        array.append(a)
        b -= a
    else:
        array.append(b)
        a -= b
    return square(a, b, array)


c = randint(1, 15)
d = randint(1, 10)
print(str(c) + ' ' + str(d))
array = square(c, d, [])
print(array)
print(len(array))
print('______________________________________ \n\n')
a = 0
for i in array:
    list = []
    print()
    for j in range(i):
        list.append(a)
    for k in range(i):
        print(list)
    a += 1

