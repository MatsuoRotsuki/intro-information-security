#include <iostream>
#include <gmpxx.h>
using namespace std;

int main(){
    mpz_class a, b;
    cout <<"a = "; cin >>a;
    cout <<"b = "; cin >>b;
    cout <<"a + b = " <<a + b <<endl
         <<"a - b = " <<a - b <<endl
         <<"a * b = " <<a * b <<endl
         <<"a / b = ";
    if (b == 0) cout <<"Error";
    else cout <<a/b;
    return 0;
}
