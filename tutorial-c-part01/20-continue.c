#include <stdio.h>

int main() {
	// your code goes here

    int x, i = 0;
    int sum = 0;

    while(i < 10) {
        i++;
        scanf("%d ", &x);
        
        if (x < 0){
            continue;
        }
        sum += x; 
    }
    printf("%d", sum);

	return 0;
}
