# Кирпа Аретмий пз3 (5-6)

# файл первый 
# задача  1

# n = input()
# print("Число Армстронга" if sum(int(d)**len(n) for d in n) == int(n) else "Не число Армстронга")


# задача 2 

# n = int(input())
# f = [0, 1]
# for i in range(2, n):
#     f.append(f[-1] + f[-2])
# print(f[:n])

# задача 3 
# import sys
# sys.setrecursionlimit(10**7)
# def f(n):
#     return n if n < 2 else f(n-1) + f(n-2)
# n = int(input())
# print([f(i) for i in range(n)])


# задача 4
 
# import sys
# sys.setrecursionlimit(10**7)
# def f(n):
#     return 1 if n < 2 else n * f(n-1)
# print(f(int(input())))

# задача 5  

# def f(s):
#     return {c: s.count(c) for c in set(s)}
# print(f(input()))


# задача 6 

# s = input()
# n = []
# for x in s.split():
#     n.append(int(x))

# t = int(input())

# r = []

# for i in range(len(n)):
#     for j in range(i + 1, len(n)):
#         if n[i] + n[j] == t:
#             r.append((n[i], n[j]))

# print(r)

# файл второй
# Арифметика в машинном коде (8-битный дополнительный код)

# a = int(input())
# b = int(input())

# def mod8(n):
#     return n % 256

# def t(n):
#     return mod8(n)

# def add8(x, y):
#     while y:
#         c = x & y
#         x = x ^ y
#         y = c < 1
#     return mod8(x)

# def sub8(x, y):
#     return add8(x, add8(mod8(~y), 1)) # ~y = -(y+1) 3

# def mul8(x, y):
#     return mod8(x * y)

# def s(x):
#     return x - 256 if x >= 128 else x

# x = t(a)
# y = t(b)

# print("Сложение:", add8(x, y), bin(add8(x, y)))
# print("Вычитание:", sub8(x, y), bin(sub8(x, y)))
# print("Умножение:", mul8(x, y), bin(mul8(x, y)))


# print("Сложение:", s(add8(x, y)))
# print("Вычитание:", s(sub8(x, y)))
# print("Умножение:", s(mul8(x, y)))



# файл третий 

# Найти представление беззнакового числа 13210 в шестнадцатиразрядном битовом наборе

# a = (bin(132)[2:])
# r = str(a)
# while len(r) <= 16:
#     r = '0'+str(r)
# print(r)

# Найти минимальное и максимальное значения чисел для 16-ти
#разрядного беззнакового представления

# minn = 0 
# maxx = 2**16 - 1 
# print(minn,maxx)

# Перевести число 12 в прямой, обратный и дополнительный код (k = 8)

# n = 12
# k = 8

# b = bin(n)[2:].zfill(k - 1)

# d = '0' + b
# b   = '0' + b
# a    = '0' + b

# print("Прямой код:", d)
# print("Обратный код:", b)
# print("Дополнительный код:", a)


# Найти прямой, обратный и дополнительный коды в однобайтовом
#представлении для числа -3510.

# n = -35
# k = 8
# b = bin(abs(n))[2:].zfill(k - 1)
# print(b)
# d = '1' + b
# b = '1' + ''.join('1' if c == '0' else '0' for c in b)
# a = bin(int(b, 2) + 1)[2:].zfill(k)
# print("Прямой код:", d)
# print("Обратный код:", b)
# print("Дополнительный код:", a)

# Задан дополнительный код числа в однобайтовом представлении:
# 1,1011100. Найти число в десятичной системе счисления.
# 1,1011100 → инверсия: 0100011 → +1: 0100100 = 36


# Дано два десятичных двузначных целых числа: А = 78, В = 56.
# Вычислить (А-В)ок, (В-А)дк.

# print("(A-B)ок =", bin(78 - 56)[2:].zfill(8))
# print("(B-A)дк =", bin((56 - 78) & 255)[2:].zfill(8))


'''
тест 
1 - B
2 - C
3 - A
4 - A 
5 - B 
6 - A 
7 - D 
8 - B 
9 - A 
10 - 103 = 01100111 - прямой 1,1100111 - обратный 1,0011000 - доп. 10011001
'''


# Для введенных чисел x и y найти значение функции
# f(x,y) =  ln sin( ) | 
# import math
# x = float(input('x: '))
# y = float(input('y: '))
# f = math.log(abs(math.sin(x + y)))
# print(f)



# # Для введенных чисел x и y найти значение функции
# import math
# x = float(input('x: '))
# y = float(input('y: '))
# s = math.sin(x + y)
# if s <= -0.5:
#     f = math.atan((3 * x - y) ** (1 / 3))
# elif s >= 0.5:
#     f = x ** 3 + y ** 1.5
# else:
#     f = math.sqrt(3) * math.log(math.fabs(x * y), 3)
# print('f =', f)


# Вычислить значение функции f(x) = cos3
# (e*x) + sin|x| на отрезке [a, b] с
# шагом hx
# import math
# a = float(input('a: '))
# b = float(input('b: '))
# h = float(input('h: '))
# x = a
# while x <= b:
#     f = math.cos(math.e * x) ** 3 + math.sin(abs(x))
#     print(f'x = {x:.3f}  f = {f:.3f}')
#     x += h



# # Вычислить значения функции
# import math

# x = 1
# while x <= 2.5:
#     y = 1
#     while y <= 4:
#         if x + y <= 2:
#             f = math.sin(x * math.exp(0.1 * y)) ** (1/3)
#         else:
#             f = math.log2(x + y)
#         print(x, y, f)
#         y += 1
#     x += 0.5