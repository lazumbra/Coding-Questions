#include <iostream>

using namespace std;

int main()
{
	long long int valueA;
	long long int valueB;

	cin >> valueA >> valueB;

	if (valueA >= valueB){
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}

	return 0;
}