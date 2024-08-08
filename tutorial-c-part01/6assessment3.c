
#include <stdio.h>

int main()
{
    // your code goes here

    float pi = 3.14, radius, diameter, circumference, area;

    scanf("%f", &radius);

    diameter = 2 * radius;
    circumference = 2 * pi * radius;
    area = pi * radius * radius;

    printf("Radius=%.2f\nDiameter=%.2f\nCircumference=%.2f\nArea=%.2f", radius, diameter, circumference, area);

    return 0;
}
