#include <stdio.h>

int main() {
	// your code goes here
	
	int a, remainder;
	
	scanf("%d", &a);
	
	remainder = a % 10;
	
	switch (remainder)
	{
		case 0:
			printf("ZERO");
			break;
			
		case 1: 
			printf("ONE");
			break;
			
		case 2: 
			printf("TWO");	
			break;
			
		case 3: 
			printf("THREE");
			break;
			
		case 4: 
			printf("FOUR");
			break;
			
		default:
			printf("GREATER THAN FOUR");
			
			
	}
	
	
	
	return 0;
}
