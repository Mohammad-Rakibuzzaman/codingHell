#include <stdio.h>

int main(){

    int a;
    scanf("%d", &a);


    int totalVal = 0;
    int iterator = 1;
    

    while (iterator <= a){
        
        totalVal += iterator;

        iterator++;
       
        
    }
    

    printf("%d", totalVal);

    return 0;
}