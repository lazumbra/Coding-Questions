#include <stdio.h>
#include <math.h> // necessário para raiz

#define NMAX 1000000 // valor máximo para o valor máximo

int main() {
    int i, j, vetor[NMAX];
    int valorMaximo, raiz;

    // Primeiro passo
    scanf("%d", &valorMaximo);

    // Segundo passo
    raiz=sqrt(valorMaximo);

    // Terceiro passo
    for (i=2; i<=valorMaximo; i++) {
        vetor[i]=i;
    }

    for(i = 0; i<20; i++){
        printf("vetor %d \n", vetor[i]);
    }

    // Quarto passo
    for (i=2; i<=valorMaximo; i++) {
        printf("num %d \n", vetor[i]);
        if (vetor[i]==i) {
            printf("%d é primo!n ", i);
            for (j=i+i; j<=valorMaximo; j+=i) {
                vetor[j]=0; // removendo da lista
            }
        }
    }

    for(i = 0; i<20; i++){
        printf("vetor 2 %d \n", vetor[i]);
    }

    return 0;
}