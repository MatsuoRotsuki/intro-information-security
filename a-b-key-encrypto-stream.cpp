#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string Encrypt(int a, int b, string x){
    string y;
    for (int i = 0; i < x.length(); i++)
        y += (char) ((a * (x[i] - 'a') + b) % 26 + 'a') ;
    return y;
}

string Decrypt(int a, int b, string x){
    string y;
}

int main (){
    int a, b, c;
    string str;
    cout << "Enter key a = ";
    cin >> a;
    cout << "Enter key b = ";
    cin >> b;
    cout << "Enter string: ";
    cin >> str;
    cout << endl << "Type 0 to encrypt, 1 to decrypt" <<endl;

    cin >> c;
}