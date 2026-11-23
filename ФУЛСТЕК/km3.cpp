// Кирпа Артемий, ЭФБО-08-26. Контрольная работа №3, вариант 8.
#include <iostream>
#include <fstream>
#include <string>
#ifdef _WIN32
#include <windows.h>
#endif
using namespace std;

// Одна буква в UTF-8 может занимать несколько байтов.
string letter(const string& s, size_t i) {
    size_t end = i + 1;
    while (end < s.size()) {
        unsigned char c = s[end];
        if (c < 128 || c >= 192) break;
        end++;
    }
    return s.substr(i, end - i);
}


// s — оставшиеся буквы, word — уже собранная часть слова.
void perm(string s, string word) {
    if (s.empty()) {
        cout << word << '\n';
        return;
    }

    for (size_t i = 0; i < s.size(); ) {
        string ch = letter(s, i);
        if (s.find(ch) == i) {  // Одинаковую букву выбираем один раз.
            string rest = s;
            rest.erase(i, ch.size());
            perm(rest, word + ch);
        }
        i += ch.size();
    }
}

int main() {
#ifdef _WIN32
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
#endif

    // №1. Перестановки строки
    string s;
    cout << "1. Введите короткую строку: ";
    getline(cin, s);
    cout << "Ответ №1. Перестановки:\n";
    perm(s, "");

    // №2. Товары дороже заданной цены
    double limit, price;
    string name;
    cout << "\n2. Введите порог цены: ";
    if (!(cin >> limit)) {
        cout << "Нужно ввести число.\n";
        return 1;
    }

    ifstream in("goods.txt");
    if (!in) {
        ofstream file("goods.txt");
        file << "35 Ручка\n80 Тетрадь\n120 Цветные карандаши\n250 Пенал\n";
        file.close();
        in.open("goods.txt");
    }

    cout << "Ответ №2. Товары дороже " << limit << ":\n";
    if (in) {
        ofstream out("result.txt");
        int count = 0;
        while (in >> price) {
            if (!getline(in >> ws, name)) break;
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
    } else {
        cout << "Не удалось открыть goods.txt.\n";
    }

    // №3. Сумма чисел
    int n;
    double x, sum = 0;
    cout << "\n3. Сколько чисел нужно сложить? ";
    if (!(cin >> n) || n < 0) {
        cout << "Нужно ввести целое число от нуля.\n";
        return 1;
    }
    if (n > 0) cout << "Введите числа через пробел: ";
    for (int i = 0; i < n; i++) {
        if (!(cin >> x)) {
            cout << "Не удалось прочитать число.\n";
            return 1;
        }
        sum += x;
    }
    cout.precision(2);
    cout << "Ответ №3. Сумма: " << fixed << sum << '\n';
    return 0;
}
