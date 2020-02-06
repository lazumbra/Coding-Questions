#include <iostream>

using namespace std;

int main()
{
	int valueA, valueB;

	cin >> valueA >> valueB;

	if (valueA % valueB == 0){
		cout << "Multiples" << endl;
	} else if (valueB % valueA == 0){
		cout << "Multiples" << endl;
	} else 
	{
		cout << "No Multiples" << endl;
	}

	return 0;
}