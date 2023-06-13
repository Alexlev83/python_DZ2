# task 1
# # data = [1, 2, 3, 5, 8, 15, 23, 38]
# # res = list()
# # for i in data:
# #     if i%2 == 0:
# #      res.append((i,i**2))
# # print(res)


# task2
# list_1 = [x for x in range(1,20)]
# print(list_1)
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# task3
# С клавиатуры вводится набор чисел через пробел. Это будут строки. Как превратить list строк в list чисел.
data ='1 2 3 5 8 15 23 38'
data = list(map(int, data.split()))

print (data)