# Кирпа Артемий ЭФБО-08-26
# задание 1.1
# import math
# def f(x):
#     return math.sqrt(2*x**2 + 1.2 - math.cos(x)) - 1
# a, b = 0.0, 1.0
# e = 1e-6
# while (b - a) / 2 > e:
#     c = (a + b) / 2
#     if f(c) == 0:
#         break
#     elif f(a) * f(c) < 0:
#         b = c
#     else:
#         a = c
# r = (a + b) / 2
# print("Приближённое значение корня уравнения:", r)
# # задание 1.2
# def ch(s, e=1e-6):
#     if s < 0:
#         raise ValueError("Корень из отрицательного числа не определён в R")
#     if s == 0:
#         return 0.0
#     a, b = 0.0, max(s, 1.0)
#     def g(x):
#         return x**2 - s
#     fa, fb = g(a), g(b)
#     while True:
#         x = a - fa * (b - a) / (fb - fa)
#         fx = g(x)
#         if abs(fx) < e or abs(b - a) < e:
#             return x
#         if fa * fx < 0:
#             b, fb = x, fx
#         else:
#             a, fa = x, fx
# try:
#     s = float(input("Введите число для извлечения квадратного корня: "))
#     r = ch(s)
#     print(f"Приближённое значение квадратного корня: {r}")
# except ValueError as ex:
#     print(f"Ошибка: {ex}")
# # задание 2.1
# def bi(a, t):
#     l, r = 0, len(a) - 1
#     p = len(a)
#     while l <= r:
#         m = (l + r) // 2
#         if a[m] == t:
#             return m, None
#         elif a[m] < t:
#             l = m + 1
#             p = l
#         else:
#             r = m - 1
#             p = m
#     return None, p
# if __name__ == "__main__":
#     a = list(map(int, input("Введите отсортированный массив чисел (через пробел): ").split()))
#     t = int(input("Введите искомый элемент: "))
#     i, p = bi(a, t)
#     if i is not None:
#         print(f"Элемент {t} найден на позиции: {i}")
#     else:
#         print(f"Элемент {t} не найден. Позиция для вставки: {p}")
#         a.insert(p, t)
#         print(f"Массив после вставки: {a}")
# # задание 2.2
# def mt(a):
#     n = len(a)
#     if n < 3:
#         return False, -1
#     l, r = 0, n - 1
#     while l < r:
#         m = (l + r) // 2
#         if a[m] < a[m + 1]:
#             l = m + 1
#         else:
#             r = m
#     p = l
#     if p == 0 or p == n - 1:
#         return False, -1
#     for i in range(1, p + 1):
#         if a[i] <= a[i - 1]:
#             return False, -1
#     for i in range(p, n - 1):
#         if a[i] <= a[i + 1]:
#             return False, -1
#     return True, p
# if __name__ == "__main__":
#     a = list(map(int, input("Введите массив (через пробел): ").split()))
#     ok, p = mt(a)
#     if ok:
#         print(f"Массив является горным. Индекс пика: {p}")
#     else:
#         print("Массив не является горным.")
# # задание 2.3
# def fn(a):
#     l, r = 0, len(a)
#     while l < r:
#         m = (l + r) // 2
#         if a[m] >= 0:
#             r = m
#         else:
#             l = m + 1
#     return l
# def fp(a):
#     l, r = 0, len(a)
#     while l < r:
#         m = (l + r) // 2
#         if a[m] > 0:
#             r = m
#         else:
#             l = m + 1
#     return l
# def cp2(a):
#     n = len(a)
#     if n == 0:
#         print("Массив пуст.")
#         return
#     cn = fn(a)
#     cp = n - fp(a)
#     print(f"Количество отрицательных: {cn}")
#     print(f"Количество положительных: {cp}")
#     if cp > cn:
#         print(f"Больше положительных. Их количество: {cp}")
#     elif cn > cp:
#         print(f"Больше отрицательных. Их количество: {cn}")
#     else:
#         print("Количество положительных и отрицательных равно.")
# if __name__ == "__main__":
#     try:
#         a = list(map(int, input("Введите отсортированный массив (через пробел): ").split()))
#         if any(a[i] > a[i+1] for i in range(len(a)-1)):
#             print("Предупреждение: массив не отсортирован по возрастанию!")
#         cp2(a)
#     except ValueError:
#         print("Ошибка ввода: введите целые числа.")
# # задание 2.4
# def ct(a):
#     n = len(a)
#     res = [0] * n
#     for i in range(n):
#         k = 0
#         for j in range(i + 1, n):
#             if a[j] < a[i]:
#                 k += 1
#         res[i] = k
#     return res
# if __name__ == "__main__":
#     a = list(map(int, input("Введите числа через пробел: ").split()))
#     print("Результат:", ct(a))
