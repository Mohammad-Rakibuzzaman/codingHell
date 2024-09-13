#include <stdio.h>

int main(){

    int a;
    scanf("%d", &a);

    int sum_total = 0;

    int i = 1; 

    while(i <= a){
        sum_total += i;
        i++;
    }

    printf("%d", sum_total);

    return 0;
}