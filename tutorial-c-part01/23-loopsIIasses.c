#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    
    int x, y;
    scanf("%d %d", &x, &y);

    for (int i = x; i <= y; i++) {
        
        if(i % 2 == 0) {
            printf("%d\n", i);
        }
        
    }

    return 0;
}
