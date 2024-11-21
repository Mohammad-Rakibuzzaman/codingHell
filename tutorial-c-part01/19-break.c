#include <stdio.h>

int main() {
	// your code goes here
    int x;
    int sum = 0;

    while(1) {

        scanf("%d", &x); 
        sum += x;

        if(sum >= 100) {
            break;
        }

        printf("%d ", sum);

    }
    
	return 0;
}
