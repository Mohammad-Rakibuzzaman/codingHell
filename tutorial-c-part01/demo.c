#include <stdio.h>

int main() {

    // with the use of scanf()

    float input_from_user;

    printf("Hi, please enter a decimal value: ");

    scanf("%f", &input_from_user);

    printf("The value that you have entered is: %0.1f", input_from_user);

    return 0;

}