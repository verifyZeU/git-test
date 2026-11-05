// #include <iostream>
// using namespace std;

// main(){
//     cout<<"hellow worls"<<endl;
//     return 0;
// }

// #include <iostream> 
// # include <cmath>


// int main() {
//     float a = 1, b = 1, x;
//     for(int i = 0;i < 10;++i)
//     x =  a - (0.1 *a * a  - a * log(a))
// }

#include <iostream>
#include <cmath> 
using namespace std;
int main() {
    double x = 1.0; 
    while (x <= 2.0) {
        if (x >= 1.0 && x <= 2.0) {
            double y = 0.1 * x * x - x * log(x);
            cout << "x = " << x <<"   "<< y << endl;
        }
        x = x + 0.1;
    }
    return 0;
}
// ''''''''''''


// #include <iostream>
// using namespace std;

// int main() {
//     int a = 1 , b = 1;
//     int k;
//     cin >> k;
//     for (int i = 0 ; i <=k ; ++i){
//     a = a * i ;
//     b = b * a ;
//     }
//     cout << b; 
// }