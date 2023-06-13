# import os
# import os.path as path1
# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# file_name = path1.join(MAIN_DIR, "Data1.txt" )

# with open (file_name, mode="rt", encoding="utf-8") as data:
#     result_list = list ()
#     for item in data:
#     #   print (*item.strip().split("#"))
#         last_name,first_name, parent = item.strip().split("#")
#         print (last_name,first_name, parent)
#         list1 = [last_name,first_name, parent ]
#         result_list.append(list1)
# print (result_list)

# №7.2[###]. Продолжение предыдущей задачи 
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо  преобразовать к виду:
# Иванов И.И.
# Петров П.П.

# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
#     В первый - в виде Иванов И.И.
#     Во второй - в виде Иванов-И-И

import os
import os.path as path1
MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR, "Data1.txt" )

with open (file_name, mode="rt", encoding="utf-8") as data:
    result_list = list ()
    for item in data:
    #   print (*item.strip().split("#"))
        last_name,first_name, parent = item.strip().split("#")
        # print (last_name,first_name, parent)
        list1 = [last_name,first_name, parent ]
        result_list.append(list1)
# print (result_list)

# Напишите функцию same_by(func, objects)
# которая проверяет, все ли элементы в objects дают одинаковое значение характеристики func
# Аргументы:
#     func - функция одного аргумента.
#     objects - список или кортеж
# Возвращаемое значение:
#     - Если  objects пустой, вернуть None
#     - Если все элементы в objects дают одинаковое значение func, вернуть True, иначе вернуть False
#
# Примеры/Тесты:
#     same_by(lambda x: x % 2, [1, 2, 10, 12]) -> False
#     same_by(lambda x: x % 2, [0, 2, 10, 12]) -> True
#     same_by(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]) ->  True
#     same_by(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
#     same_by(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
#     same_by(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> True
#     same_by(lambda x: x[0], ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) ->  False
#     same_by(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]) ->  True