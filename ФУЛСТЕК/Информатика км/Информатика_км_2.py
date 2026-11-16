# Group: ЭФБО-08-26
# Student: Кирпа Артемий

print("=== Задание 1 ===")
bit_hex = 4
n = 16
bits = n * bit_hex
byts = bits / 8
print("Одна hex-цифра:", bit_hex, "бита")
print("Объём в битах:", bits)
print("Объём в байтах:", byts)
print("Ответ: 64 бита = 8 байт")


print()
print("=== Задание 2 ===")


def f2(a, b, c):
    return (a | b) ^ c


print("A B C | F")
k = 0
for a in range(2):
    for b in range(2):
        for c in range(2):
            r = f2(a, b, c)
            print(a, b, c, "|", r)
            if r == 1:
                k += 1
print("Количество строк, где F = 1:", k)


print()
print("=== Задание 3 ===")


def f(a: bool, b: bool, c: bool) -> bool:
    return (a and c) or ((not a) and b)


ok = True
for a in (False, True):
    for b in (False, True):
        for c in (False, True):
            old = ((a or b) and ((not a) or c)) or (a and c)
            if old != f(a, b, c):
                ok = False
print("Итог: F = (A & C) v (~A & B)")
print("Проверка с исходной формулой:", "верно" if ok else "ошибка")


print()
print("=== Задание 4 ===")


def pool(t, s, al):
    return int(t == 1 and s == 0 and al == 0)


print("Turbid ServiceMode Alarm | FilterOn")
for t in range(2):
    for s in range(2):
        for al in range(2):
            print("  ", t, "      ", s, "       ", al, "   |  ", pool(t, s, al))

print("Пример ввода: 1 0 0")
print("Пример вывода:", pool(1, 0, 0))
print("Пример ввода: 1 1 0")
print("Пример вывода:", pool(1, 1, 0))


print()
print("=== Задание 5 ===")


def f5(x, y, z):
    return ((1 - x) & (1 - y) & z) | (x & (1 - z))


nab = [(0, 0, 1), (1, 0, 0), (1, 1, 0)]
ok = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            need = 1 if (x, y, z) in nab else 0
            if f5(x, y, z) != need:
                ok = False
print("Минимальная форма: f = (~x & ~y & z) v (x & ~z)")
print("Проверка по наборам:", "верно" if ok else "ошибка")


print()
print("=== Задание 6 ===")


def mux(a: int, b: int, s0: int, s1: int) -> int:
    y1 = (1 - s0) & (1 - a) & b
    y2 = s0 & (1 - s1) & a & b
    y3 = s0 & s1 & (1 - a)
    return y1 | y2 | y3


def mux_old(a, b, s0, s1):
    i0 = (1 - a) & b
    i1 = a & b
    i2 = (1 - a) & b
    i3 = 1 - a
    if s1 == 0 and s0 == 0:
        return i0
    if s1 == 0 and s0 == 1:
        return i1
    if s1 == 1 and s0 == 0:
        return i2
    return i3


ok = True
print("A B S0 S1 | Y")
for a in range(2):
    for b in range(2):
        for s0 in range(2):
            for s1 in range(2):
                y = mux(a, b, s0, s1)
                print(a, b, s0, " ", s1, "|", y)
                if y != mux_old(a, b, s0, s1):
                    ok = False
print("Проверка с исходным мультиплексором:", "верно" if ok else "ошибка")


print()
print("=== Задание 7 ===")


def f7(a: int, b: int, c: int) -> int:
    return (1 - b) & (a | (1 - c))


tab = {(0, 0, 0): 1, (0, 0, 1): 0, (0, 1, 0): 0, (0, 1, 1): 0,
       (1, 0, 0): 1, (1, 0, 1): 1, (1, 1, 0): 0, (1, 1, 1): 0}
ok = True
print("A B C | F")
for k in tab:
    r = f7(k[0], k[1], k[2])
    print(k[0], k[1], k[2], "|", r)
    if r != tab[k]:
        ok = False
print("Минимальная форма: F = ~B & (A v ~C)")
print("Проверка по таблице:", "верно" if ok else "ошибка")