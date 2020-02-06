#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    cout << fixed << setprecision(9);
    float number_compute, result;
    float pi = 3.141592653;
    cin >> number_compute;
    result = (number_compute * number_compute) * pi;
    cout << result << endl;
    return 0;
}