#include <stdio.h>

int main(){

    int a, b, isBothZero, isNotBothZero;
    scanf("%d %d", &a, &b);

    isNotBothZero = (a != 0) || (b != 0);
    isBothZero = !isNotBothZero;

    printf("bothZeroes: %d", isBothZero);


    return 0;
}