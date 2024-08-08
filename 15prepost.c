#include <stdio.h>

int main(){

    int a = 1;
    int result = ++a;
    printf("%d\n", result);
    result = a++; 
    printf("%d", result); 


    return 0;
}