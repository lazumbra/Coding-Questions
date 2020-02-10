#include <stdio.h>

void update(int *a,int *b) {
    int valA = *a;
    valA = *a + *b;
    *b = *a - *b;
    *a = valA;
    if (*b < 0){
        *b = -1 * *b;
    }
    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

