#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int len_for;
    cin >> len_for;
    int arr[len_for];

    for(int i = 0; i < len_for; i++){
        int value_user;
        cin >> value_user;
        arr[i] = value_user;

    }

    for(int i = len_for-1; i >= 0; i--){
        cout << arr[i] << " ";
    }
    
    return 0;
}
