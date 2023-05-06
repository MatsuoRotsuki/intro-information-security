#include <iostream>

using namespace std;

int modInverse(long long a, long long m){
	for (long long i = 1; i < m; i++){
		if (((a%m) * (i%m)) % m == 1)
			return i;
	}
	return -1;
}

int main (){
	long long a = 15;
	long long m = 2305843009213693951;
	printf("%ld", modInverse(a,m));
}
