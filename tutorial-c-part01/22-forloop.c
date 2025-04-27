// #include<stdio.h>
// int main() {
//     int iterator = 1;
//     while (iterator <= 5) {
//         printf("%d\n", iterator);
//         iterator++;
//     }
//     return 0;
// }

// #include<stdio.h> 
// int main() { 
//     for(int i = 1; i <= 5; i++ ){
//         printf("%d\n", i);
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main(void)
// {
//     int n;
//     int sum = 0;
//     scanf("%d", &n);

//     for(int i = 1; i <= n; i++){
//         sum += i;
//     }
//     printf("%d", sum);


//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main(void)
// {
    
//     int i = 5;
//     for (;;) {
//         if (i < 1) {
//             break;
//         }
//         printf("%d ", i);
//         i--;
//     }
//     return 0;
// }




// #include <stdio.h>
// #include <stdlib.h>

// int main(void)
// {
    
//     int n;
//     int sum = 0;

//     for(int i = 0; i < 10; i++) {
//         scanf("%d ", &n);


//         if (n > 0) {
//             sum += n;
//         } else {
//             break;
//         }
//     }

//     // int i = 0;
//     // while (i < 10) {
//     //     scanf("%d ", &n);

//     //     if (n > 0) {
//     //         sum += n;
//     //     } else {
//     //         break;
//     //     }


//     //     i++;
//     // }

//     printf("%d", sum);

//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main(void)
// {
    
//     int sum = 0;

//     for (int i=0; i < 10; i++) {
//         int n;
//         scanf("%d", &n);    

//         if (n >= 0) {
//             sum += n;
//         } else {
//             continue;
//         }

//     }

//     printf("%d", sum);

//     return 0;
// }
// int main () {
//     int i;
//     for (i = 0; i < 5; i++) {
//         printf("%d\n", i);
//     }

//     for (; i < 10; i++) {
//         printf("%d\n", i);
//     }
// }

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i;
    
    // Start with 0, loop till 5 (inclusive) using ++
    for (i = 0; i <= 5; i++) {
        printf("%d\n", i);
    }

    // Loop back to 0 (inclusive) using --
    for (i = 4; i >= 0; i--) {
        printf("%d\n", i);
    }

    // Loop till 10 (inclusive) using +=2
    for (i = 2; i <= 10; i += 2) {
        printf("%d\n", i);
    }

    // Loop back to 1 (inclusive) using /=2
    for (i = 5; i >= 1; i /= 2) {
        printf("%d\n", i);
    }
    
    // Loop till 10 (inclusive) using *=2
    for (i = 2; i <= 10; i *= 2) {
        printf("%d\n", i);
    }

    // Loop back to 0 (inclusive) using -=2
    for (i = 6; i >= 0; i -= 2) {
        printf("%d\n", i);
    }

    return 0;
}
