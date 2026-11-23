// Кирпа Артемий, ЭФБО-08-26. Контрольная работа №3, часть 1, вариант 8.
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <utility>
#ifdef _WIN32
#include <windows.h>
#endif

using namespace std;

// Задание 1. По очереди ставим каждую букву на место k.
void perm(vector<string>& a, int k) {
    int n = a.size();
    if (k == n) {
        for (const string& ch : a) cout << ch;
        cout << '\n';
        return;
    }

    string used;
    for (int i = k; i < n; i++) {
        if (used.find(a[i]) != string::npos) continue;
        used += a[i];
        swap(a[k], a[i]);
        perm(a, k + 1);
        swap(a[k], a[i]);
    }
}

int main() {
#ifdef _WIN32
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
#endif

    // Задание 1. Выводим перестановки строки.
    string s;
    cout << "1. Введите короткую строку: ";
    getline(cin, s);

    // Буква в UTF-8 может занимать несколько байтов.
    vector<string> a;
    for (unsigned char c : s) {
        if ((c & 0xC0) != 0x80) a.push_back("");
        a.back() += static_cast<char>(c);
    }

    cout << "Ответ №1. Перестановки:\n";
    perm(a, 0);

    // Задание 2. Отбираем товары из файла по цене.
    cout << "\n2. Введите порог цены: ";
    double limit, price;
    if (!(cin >> limit)) return 1;

    ifstream in("goods.txt");
    if (!in) {
        ofstream sample("goods.txt");
        sample << "35 Ручка\n80 Тетрадь\n120 Цветные карандаши\n250 Пенал\n";
        sample.close();
        in.open("goods.txt");
    }

    cout << "Ответ №2. Товары дороже " << limit << ":\n";
    if (!in) {
        cout << "Не удалось открыть goods.txt.\n";
    } else {
        ofstream out("result.txt");
        string name;
        int count = 0;
        while (in >> price && getline(in >> ws, name)) {
            if (price > limit) {
                cout << name << " — " << price << '\n';
                out << name << " — " << price << '\n';
                count++;
            }
        }
        if (count == 0) cout << "Таких товаров нет.\n";
        out.close();
        if (out) cout << "Записано в result.txt: " << count << '\n';
        else cout << "Не удалось записать result.txt.\n";
    }

    // Задание 3. Складываем числа.
    int n;
    double x, sum = 0;
    cout << "\n3. Сколько чисел нужно сложить? ";
    if (!(cin >> n) || n < 0) {
        cout << "Введите целое неотрицательное количество.\n";
        return 1;
    }
    if (n > 0) cout << "Введите числа через пробел (например, 1.5 2.75): ";
    for (int i = 0; i < n; i++) {
        if (!(cin >> x)) {
            cout << "Не удалось прочитать число.\n";
            return 1;
        }
        sum += x;
    }
    cout << "Ответ №3. Сумма: " << fixed << setprecision(2) << sum << '\n';
    return 0;
}
