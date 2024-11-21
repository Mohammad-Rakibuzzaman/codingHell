#include <stdio.h>

int main() {
	// your code goes here


    int x;
    int sum = 0;
    scanf("%d", &x);

    while(x >= 1) {
        sum = sum + x;
        x--;
    }

    printf("%d", sum);
    
	return 0;
}