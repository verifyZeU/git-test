# Кирпа Артемий 
# ЭФБО-08-26 

# ЗАДАЧА 1.1 
# for a in range(2):
#     for b in range(2):
#         f = (a or b) <= (a == b)
#         print(a,b,f)

# # ЗАДАЧА 1.2
# for a in range(2):
#     for b in range(2):
#         f = ((not(a)) or ((not(b)) == (not(a)))) != b
#         print(a,b,f)

# ЗАДАЧА 1.3
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             f = (not(a or b)) or c 
#             print(a,b,c,f)


# Задание 2
# s = ["арбуз", "кресло", "ответ", "привет"]
# for x in s:
#     a = x[0] in "аеёиоуыэюя"
#     b = x[4] not in "аеёиоуыэюя"
#     c = x[1] in "аеёиоуыэюя"
#     if (not (a or b)) or c:
#         print(x)




# Задание 3
# for a in [0, 1]:
#     for b in [0, 1]:
#         for c in [0, 1]:
#             f = (not ((not a) or b)) and (not c)
#             f1 = (not a) and b and (not c)
#             f2 = a and (not b) and (not c)
#             f3 = (not a) and (not b) and (not c)
#             f4 = a and b and (not c)
#             if f == f1:
#                 print("1")
#             if f == f2:
#                 print("2")
#             if f == f3:
#                 print("3")
#             if f == f4:
#                 print("4")



# Задание 4
# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             f = 0
#             if x == 0 and y == 0 and z == 0:
#                 f = 0
#             if x == 1 and y == 0 and z == 1:
#                 f = 1
#             if x == 0 and y == 1 and z == 0:
#                 f = 1
#             f1 = (not x) and (not y) and z
#             f2 = (not x) and y and z
#             f3 = (not x) and y and (not z)
#             f4 = x or (y and (not z))
#             if f == f1:
#                 print("Ответ: 1")
#             if f == f2:
#                 print("Ответ: 2")
#             if f == f3:
#                 print("Ответ: 3")
#             if f == f4:
#                 print("Ответ: 4")



# Задание 5
# x = 1
# while True:
#     f1 = (x + 6) * x + 9 > 0
#     f2 = x * x > 20
#     f = (not f1) or f2
#     if not f:
#         print(x)
#     x += 1
#     if x > 10:
#         break


# Задание 6
# for a in [0, 1]:
#     for b in [0, 1]:
#         for c in [0, 1]:
#             for d in [0, 1]:
#                 f1 = not ((c or b) and a)
#                 f2 = ((not a) and (not c)) or d
#                 f = (not f1) or f2
#                 if not f:
#                     print(a, b, c, d)




# Задание 7
# from itertools import permutations
# n = ["Аня", "Надя", "Вера", "Лиза", "Саша"]
# for p in permutations([1, 2, 3, 4, 5]):
#     a = p[0]
#     f = p[1]
#     v = p[2]
#     l = p[3]
#     s = p[4]
#     x1 = (a == 1) + (l == 3)
#     x2 = (v == 5) + (f == 1)
#     x3 = (s == 1) + (v == 2)
#     x4 = (l == 5) + (f == 4)
#     x5 = (f == 4) + (a == 1)
#     if x1 == 1 and x2 == 1 and x3 == 1 and x4 == 1 and x5 == 1:
#         print("Саша:", s)
#         print("Аня:", a)

# 8
# k = 0
# for a in [0, 1]:
#     for b in [0, 1]:
#         for c in [0, 1]:
#             for d in [0, 1]:
#                 for e in [0, 1]:
#                     f = a and (not b) and c and (not d) and (e or (not e))
#                     if not f:
#                         k += 1
# print(k)


# 9
# x = 1
# while x < 100:
#     f1 = 100 < x * x
#     f2 = 100 > (x + 1) * (x + 1)
#     f = (not f1) or f2
#     if f:
#         print(x)
#     x += 1


# 10
# from itertools import permutations
# c = ["красная", "черная", "белая", "синяя"]
# for p in permutations(c):
#     a = p[0]
#     m = p[1]
#     n = p[2]
#     v = p[3]
#     s1 = (a == "красная") and (m == "черная")
#     s2 = (a == "черная") and (v == "белая")
#     s3 = (n == "черная") and (v == "синяя")
#     if s1 + s2 + s3 == 1:
#         print("Михаил:", m)
#         print("Виктор:", v)


# тест 
'''
1 - 2
2-1
3-2
4-1
5-4
6-1
7-3
8-30
9-10
10-М,Б
'''


# задачи из вордовского файла 
# задача 1 
'''
def identify_mages(mages):
    names = ['A', 'B', 'C', 'D', 'E']
    # Вопрос, который одинаково работает для truth и lie.
    def ask(i, q):
        return mages[i](lambda: q)
    # Спрашиваем мага, является ли другой маг случайным.
    def is_random(i, j):
        ans = mages[i](
            lambda: mages[j](lambda: True) == 'zor'
        )
        return ans == 'zor'
    # Проверяем кандидата несколько раз.
    def check(i):
        a = []
        for j in range(5):
            if i != j:
                a.append(is_random(i, j))
        # Если маг считает двух или больше других случайными,
        # это подозрительно.
        return sum(a)
    # Ищем мага, который выглядит наиболее согласованным.
    scores = []
    for i in range(5):
        scores.append(check(i))
    # Маг с наименьшим количеством "случайных" ответов
    # используется как опорный.
    good = scores.index(min(scores))
    ans = {}
    # Определяем остальных относительно опорного мага.
    for i in range(5):
        if i == good:
            continue
        x = mages[good](
            lambda i=i: mages[i](lambda: True) == 'zor'
        )
        if x == 'zor':
            ans[names[i]] = 'truth'
        else:
            ans[names[i]] = 'lie'
    # Опорный маг считается truth/lie,
    # если остальные ответы согласуются с ним.
    ans[names[good]] = 'truth'
    # Ищем магов, которые дают противоречивые ответы.
    for i in range(5):
        if i == good:
            continue
        n = 0
        for j in range(5):
            if i != j:
                x = mages[i](
                    lambda j=j: mages[j](lambda: True) == 'zor'
                )
                if x == 'zor':
                    n += 1
        if n == 0 or n == 4:
            ans[names[i]] = 'random'
    return ans
'''


# задача 2 
def identify_potions(potions):
    names = ['A', 'B', 'C', 'D', 'E']
    ans = {}
    for i in range(5):
        # Первый тест
        x = potions[i](lambda: True)
        # Второй тест с противоположным утверждением
        y = potions[i](lambda: False)
        if x == 'success' and y == 'fail':
            ans[names[i]] = 'true'
        elif x == 'fail' and y == 'success':
            ans[names[i]] = 'false'
        else:
            ans[names[i]] = 'random'
    return ans