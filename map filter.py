# numbers = ["3","34","64"]
# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i])
# numbers = list(map(int,numbers))
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a

# num = [2,3,5,4,6,66,3,3,2]
# # square = list(map(sq,num))
# square = list(map(lambda x: x*x, num))
# print(square)
#
# def sq(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [sq,cube]
# for i in range(5):
#     var = list(map(lambda x:x(i),func))
#     print(var)

# list_1 = [1,2,3,4,5,6,7,8]
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5,list_1))
# print(gr_than_5)

from functools import reduce
list1 = [1,2,3,4,5,6]
num = reduce(lambda x,y:x*y,list1)
print(num)