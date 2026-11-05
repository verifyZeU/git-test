#Кирпа Артемий
#Практическо задание номер 4 


# задание 1 
# a = int(input()) # число которое переводим в 10 систему
# b = int(input()) #  начальная система 
# print(int(str(a),b))



#ЗАДАНИЕ 2 
# a = int(input())
# b = int(input())
# s = '' 
# while a > 0:
#     s = str(a % b) + s
#     a = a // b 
# print(s)

#ЗАДАНИЕ 3 
# a = int(input())
# b = int(input())
# def f(a, b):
#     if a == 0:
#         return "0"
#     p = 0
#     while b ** (p + 1) <= a:
#         p += 1
#     r = []
#     for i in range(p, -1, -1):
#         c = a // (b ** i)
#         r.append(str(c))
#         a = a % (b ** i)
#     return ''.join(r)
# print(f(a,b))  

#задание 4 
# a = int(input()) # число
# b = int(input()) # до  
# c = int(input()) #  после 
# s = '' 
# w = ''
# if c == 10: 
#     print(int(str(a),b))
# if b == 10: 
#     while a > 0:
#         s = str(a%c) + s 
#         a = a//c
#     print(s) 
# if b != 10 and c != 10:
#     q = (int(str(a),b)) 
#     while q > 0:
#             w = str(q%c) + w
#             q =q//c
#     print(w) 


# ЗАДАНИЕ 5 
'''
a = int(input())  
b = int(input())  
c = int(input())  
s = ''
w = ''
ori = a  

def to(num, l):
    return int(str(num), l)

def fr(num, l):
    if num == 0:
        return "0"
    r = ''
    while num > 0:
        r = str(num % l) + r
        num = num // l
    return r

if c == 10:
    r = to(a, b)
    print(r)
    res = fr(r, b)
    cor = str(a) == res
    print(cor,res)

elif b == 10:
    while a > 0:
        s = str(a % c) + s
        a = a // c
    if s == '':
        s = '0'
    res = s
    print(res)
    res = to(res, c)
    cor = ori == res
    print(cor,res)

else:  # b != 10 and c != 10
    q = to(a, b)  # 
    tem = q  
    while q > 0:
        w = str(q % c) + w
        q = q // c
    if w == '':
        w = '0'
    res = w
    print(res)
    dec = to(res, c)
    restorg = fr(dec, b)
    iscor = str(a) == restorg
    print(iscor)
    print(dec)
    print(restorg)
'''


# ЗАДАНИЕ 6  
# import math
# def le(n, b):
#     if n == 0:
#         return 1
#     return math.floor(math.log(n, b)) + 1
# num = 1000
# for b in range(2, 17):
#     if num == 0:
#         e = 1
#     else:
#         temp = num
#         e = 0
#         while temp > 0:
#             temp //= b
#             e += 1
#     t = le(num, b)
#     print(f"{b:<10} {e:<12} {t:<10}")


#ЗАДАНИЕ 7 
# n = int(input())
# for b in [2, 8, 10, 16, 36]:
#     res, x = '', n
#     while x:
#         res = '0123456789ABCDEF' [x % b] + res
#         x //= b
#     print (b,res)

# # ЗАДАНИЕ 8
# n = input().upper()
# base = int(input())
# digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# if all(c in digits[:base] for c in n):
#     print ('+')
# else:
#     print("-")