# Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :

# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Напишите функцию

# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.

# a = int(input('Введите первый элемент прогрессии :'))
# b = int(input('Введите разность :'))
# n = int(input('Введите количество элементов :'))
# result = []
# for i in range(n):
#    result.append(a)
#    a+=b 
#    result = result[::1]

# print(result)

# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)
# def index (list1: list) -> list:
min = 2
max= 10
list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
result = list()
for i in range(len(list1)):
 if  min <= list1[i] <= max:
     result.append(list1[i])
print (sorted(result))