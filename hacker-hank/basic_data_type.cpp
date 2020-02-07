#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int valueA; long int valueB; 
    char valueC; 
    float valueD; 
    double valueE;
    cin >> valueA >> valueB >> valueC >> valueD >> valueE;

    printf("%d\n", valueA);
    printf("%ld\n", valueB);
    printf("%c\n", valueC);
    printf("%f\n", valueD);
    printf("%lf", valueE);
    return 0;
}