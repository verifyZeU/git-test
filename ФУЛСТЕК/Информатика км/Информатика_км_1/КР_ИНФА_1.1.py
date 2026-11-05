# Кирпа Артемий ЭФБО-08-26

# задание 1 
# n = 24          # символов
# b = 2           # байт на символ
# byte = n * b    # байт всего
# bit = byte * 8  # бит всего
# print(byte, "байт")
# print(bit, "бит")

# задание 2 
# n = 2023
# s = bin(n)[2:]     
# print(s)
# print(len(s), "разрядов")

# задание 3
# x = "11011010"
# print("Дополнительный код:", x)
# if x[0] == "1":
#     y = ""

#     for i in x:
#         if i == "0":
#             y = y + "1"
#         else:
#             y = y + "0" # инвертирование битов

#     n = int(y, 2) + 1
#     n = -n
#     print("Знак: отрицательный")
#     print("Число:", n)
#     p = bin(abs(n))[2:].zfill(7)
#     p = "1" + p
#     o = "1"

#     for i in p[1:]:
#         if i == "0":
#             o = o + "1"
#         else:
#             o = o + "0" # инвертирование битов

#     print("Прямой код:", p)
#     print("Обратный код:", o)
# else:
#     n = int(x, 2)
#     print("Знак: положительный")
#     print("Число:", n)

# задание 4
# a = [0xAA, 0x55, 0x00, 0x03]
# print("Пакет:")
# for x in a:
#     print(hex(x), end=" ")
# print()
# s = 0
# for i in range(len(a) - 1):
#     s = s + a[i]
# s = s % 256
# # print(s,a[-1])
# print()
# print("Правильная checksum:", hex(s))
# print("Checksum в пакете:", hex(a[-1]))
# if s == a[-1]:
#     print("Ошибок нет")
# else:
#     print("ОШИБКА CHECKSUM!")