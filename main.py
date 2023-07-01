# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n = int(input('Введите число n= '))

i, degree_two = 0, 1

while degree_two < n:
    print(degree_two, end=" ")
    i += 1
    degree_two = 2 ** i
