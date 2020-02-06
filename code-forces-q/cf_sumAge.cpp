#include <iostream>

using namespace std;

int main()
{
	int idade;
	cin >> idade;
	int somatorio = 0;
	for(int i = 1; i < idade+1; i++){
		somatorio += i;
	}
	cout << somatorio << endl;
	return 0;
}