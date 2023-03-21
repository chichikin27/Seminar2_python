# number = int(input()) 
# factorial = 1 
 
# while number > 0: 
#     factorial = factorial * number 
#     number = number - 1 
# print(factorial)


# num = int(input('enter num: '))
# fib1 = 1
# fib2 = fib1
# fib = fib2
# coint = 3

# while num > fib:
#     fib = fib1 + fib2 
#     fib1 = fib2
#     fib2 = fib
#     coint += 1

# if num == fib:
#     print(coint)
# else:
#     print(-1)


# count_days = int(input())
# days = []
# day = None
# count = 0
# count1 = 0
# count2 = 0
# while count < count_days:
#     day = int(input('Введите показания: '))
#     days.append(day)
#     count += 1
# print(days)

# for i in days:
#     if i > 0:
#         count1 += 1
#     else:
#         count2 -= 1
# print(count1)

# import random
# from random import randint

# qu = int(input('Введите колиество арбузов: '))
# max = 0
# mass = []

# for i in range(qu):
#     mass.append(randint(5, 25))

# print(mass)

# print('=========================')

# for i in range(len(mass)):
#     if mass[i] >= max:
#         max = mass[i]
# print(max)
# print('=========================')
# min = mass[0]
# for j in range(len(mass)):
#     if mass[j] <= min:
#         min = mass[i]
# print(min)