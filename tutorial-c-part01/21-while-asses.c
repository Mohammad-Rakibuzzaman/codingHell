#include <stdio.h>

int main() {

    int i = 0, num;
    while (i < 6){
        i++;
        scanf("%d", &num);
        
        if (num  <= 0) {
            break;
        } 
        if (num < 100) {
         
            printf("%d ", num * num);
        }

    }

    return 0;
}