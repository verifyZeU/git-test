// Студент: Кирпа Артемий
// Группа: ЭФБО-08-26
// Вариант: 8 



// ЗАДАНИЕ 1, №8
// #include <iostream>
// #include <clocale>
// using namespace std;
// int main() {
//     setlocale(LC_ALL, "Russian");
//     int a[6] = {5, 8, 2, 9, 1, 7}; // исходный массив
//     int b[6];                      // сюда скопируем
//     int n = 6;
//     cout << "Исходный массив: ";
//     for (int i = 0; i < n; i++) cout << a[i] << " ";
//     cout << endl;
//     // копируем a в b
//     for (int i = 0; i < n; i++) b[i] = a[i];
//     cout << "Новый массив: ";
//     for (int i = 0; i < n; i++) cout << b[i] << " ";
//     cout << endl;
//     return 0;
// }


// ЗАДАНИЕ 2, №8
// (решение двумя способами)
#include <iostream>
#include <clocale>
using namespace std;
int main() {
    setlocale(LC_ALL, "Russian");
    int n = 4;
    int a[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    cout << "Матрица:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << a[i][j] << "\t";
        cout << endl;
    }
    // Способ 1: проверяем условие i + j > n - 1 
    cout << "Способ 1 (через условие): ";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (i + j > n - 1) cout << a[i][j] << " ";
    cout << endl;
    // Способ 2: сразу берем нужные столбцы, без условия
    // в строке i элементы ниже побочной диагонали идут от столбца n - i до n - 1
    cout << "Способ 2 (через границы цикла): ";
    for (int i = 1; i < n; i++)
        for (int j = n - i; j < n; j++)
            cout << a[i][j] << " ";
    cout << endl;
    return 0;
}


// // ЗАДАНИЕ 3, №8
// #include <iostream>
// #include <clocale>
// using namespace std;
// int big(int a, int b) {
//     if (a > b) return a;
//     return b;
// }
// main z3() {
//     int x, y;
//     cout << "Введите два числа: ";
//     cin >> x >> y;
//     cout << "Большее: " << big(x, y) << endl;
// }

// int main() {
//     setlocale(LC_ALL, "Russian");
//     cout << "--- Задание 1, №8 ---" << endl;
//     z1();
//     cout << endl << "--- Задание 2, №8 ---" << endl;
//     z2();
//     cout << endl << "--- Задание 3, №8 ---" << endl;
//     z3();
//     return 0;
// }



///////////////////////////////////
// Студент: Кирпа Артемий
// Группа: ЭФБО-08-26
// Вариант: 8 

// ЗАДАНИЕ 1, №8
#include <iostream>
#include <clocale>
using namespace std;
int main() {
    int a[6] = {5, 8, 2, 9, 1, 7}; // исходный массив
    int b[6];                      // сюда скопируем
    int n = 6;
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    // копируем a в b
    for (int i = 0; i < n; i++) b[i] = a[i];
    for (int i = 0; i < n; i++) cout << b[i] << " ";
    cout << endl;
    return 0;
}

// // ЗАДАНИЕ 2, №8
// // (решение двумя способами)
// #include <iostream>
// #include <clocale>
// using namespace std;
// int main() {
//     setlocale(LC_ALL, "Russian");
//     int n = 4;
//     int a[4][4] = {
//         {1, 2, 3, 4},
//         {5, 6, 7, 8},
//         {9, 10, 11, 12},
//         {13, 14, 15, 16}
//     };
//     cout << "Матрица:" << endl;
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) cout << a[i][j] << "\t";
//         cout << endl;
//     }
//     // Способ 1: проверяем условие i + j > n - 1 
//     cout << "Способ 1 (через условие): ";
//     for (int i = 0; i < n; i++)
//         for (int j = 0; j < n; j++)
//             if (i + j > n - 1) cout << a[i][j] << " ";
//     cout << endl;
//     // Способ 2: сразу берем нужные столбцы, без условия
//     // в строке i элементы ниже побочной диагонали идут от столбца n - i до n - 1
//     cout << "Способ 2 (через границы цикла): ";
//     for (int i = 1; i < n; i++)
//         for (int j = n - i; j < n; j++)
//             cout << a[i][j] << " ";
//     cout << endl;
//     return 0;
// }




// // ЗАДАНИЕ 3, №8
// #include <iostream>
// #include <clocale>
// using namespace std;
 
// // функция big возвращает большее из двух чисел
// int big(int a, int b) {
//     if (a > b) return a;
//     return b;
// }
// int main() {
//     setlocale(LC_ALL, "Russian");
//     int x = 5, y = 9;
//     cout << "Числа: " << x << " и " << y << endl;
//     cout << "Большее: " << big(x, y) << endl;
//     x = 20;
//     y = 3;
//     cout << "Числа: " << x << " и " << y << endl;
//     cout << "Большее: " << big(x, y) << endl;
//     return 0;
// }


















// Студент: Кирпа Артемий
// Группа: ЭФБО-08-26
// Вариант: 8 

// ЗАДАНИЕ 1, №8
// #include <iostream>
// using namespace std;
// int main() {
//     int a[6] = {5, 8, 2, 9, 1, 7}; // исходный массив
//     int b[6];                      // сюда скопируем
//     int n = 6;
//     for (int i = 0; i < n; i++) cout << a[i] << " ";
//     cout << endl;
//     // копируем a в b
//     for (int i = 0; i < n; i++) b[i] = a[i];
//     for (int i = 0; i < n; i++) cout << b[i] << " ";
//     cout << endl;
//     return 0;
// }

// // ЗАДАНИЕ 2, №8
// (решение двумя способами)
// #include <iostream>     
// using namespace std;
// int main() { 
//     int n = 4;
//     int a[4][4] = {
//         {1, 2, 3, 4},
//         {5, 6, 7, 8},
//         {9, 10, 11, 12},
//         {13, 14, 15, 16}
//     }; // j - кол-во столбцов       i - колво строк 
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) cout << a[i][j] << "\t";
//         cout << endl;
//     }
//     // Способ 1: проверяем условие i + j > n - 1 
//     for (int i = 0; i < n; i++)
//         for (int j = 0; j < n; j++)
//             if (i + j > n - 1) cout << a[i][j] << " ";
//     cout << endl;   
//     // Способ 2: сразу берем нужные столбцы, без условия
//     // в строке i элементы ниже побочной диагонали идут от столбца n - i до n - 1
//     for (int i = 1; i < n; i++)
//         for (int j = n - i; j < n; j++)
//             cout << a[i][j] << " ";
//     cout << endl;
//     return 0;
// }




// // ЗАДАНИЕ 3, №8
// #include <iostream>
// using namespace std;
// int big(int a, int b) {
//     if (a > b) return a;
//     return b;
// }
// int main() {
//     int x = 5, y = 9;
//     cout << x << " " << y;
//     cout << " - " << big(x, y) << endl;
//     x = 20;
//     y = 3;
//     cout << x << " " << y;
//     cout << " - " << big(x, y);  
//     return 0;
// }    