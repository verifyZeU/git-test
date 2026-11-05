//Кирпа Артемий ЭФБО-08-26
// задание 1 

// #include <iostream>
// using namespace std;
// int main() {
//     int n;
//     cin >> n;
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             if (i + j < n - 1)
//                 cout << 0;
//             else if (i + j == n - 1)
//                 cout << 1;
//             else
//                 cout << 2;
//         }
//         cout << endl;
//     }
//     return 0;
// }


// задание 1 (доп способ)

// #include <iostream>
// using namespace std;

// int main() {
//     int n;
//     cin >> n;
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n - i - 1; j++)
//             cout << 0;
//         cout << 1;
//         for (int j = 0; j < i; j++)
//             cout << 2;

//         cout << endl;
//     }
//     return 0;
// }



// задание 2 
// #include <iostream>
// using namespace std;
// int main() {
//     int n, m, w;
//     int a[32][32] = {};
//     cin >> n >> m >> w;
//     // Записываем грибы
//     for (int i = 0; i < w; i++) {
//         int x, y;
//         cin >> x >> y;
//         a[x - 1][y - 1] = -1;
//     }
//     // Считаем грибы рядом
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < m; j++) {
//             if (a[i][j] != -1) {
//                 for (int x = i - 1; x <= i + 1; x++) {
//                     for (int y = j - 1; y <= j + 1; y++) {
//                         if (x >= 0 && x < n && y >= 0 && y < m) {
//                             if (a[x][y] == -1) {
//                                 a[i][j]++;
//                             }
//                         }
//                     }
//                 }
//             }
//         }
//     }
//     // Выводим карту
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < m; j++) {
//             if (a[i][j] == -1)
//                 cout << '*';
//             else
//                 cout << a[i][j];
//         }
//         cout << endl;
//     }
//     return 0;
// }




// задангие 3 
#include <iostream>
#include <string>
using namespace std;

int main() {
    int x, n;
    string s;
    cin >> x >> n;
    s = to_string(x);
    for (int i = 1; i < n; i++) {
        string t = "";
        for (int j = 0; j < s.size(); j++) {
            int k = 1;
            while (j + 1 < s.size() && s[j] == s[j + 1]) {
                k++;
                j++;
            }
            t += to_string(k);
            t += s[j];
        }
        s = t;
    }
    cout << s;
    return 0;
}
