#include <iostream>

using namespace std;

int modexponen(int a, int b, int n){
	if (b == 0) return 1;
	if (b == 1) return a;
	int r = modexponen(a, b/2, n);
	r = (r*r) % n;
	if (b % 2 == 1) r = (r*a) % n;
	return r % n;
}

int main (){
	int x = 18446744073709551629;
	int y = 5;
	int n = 1125899906842679;
	cout << modexponen(x, y ,n);
}
