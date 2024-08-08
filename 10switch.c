#include <stdio.h>

int main() {
	// your code goes here
	int a;
	
	scanf("%d", &a);
	
	switch (a%2){
			
		case 1:
			printf("ODD");
			break;
			
		// case 0:
		// 	printf("EVEN");
		// 	break;
		default:
            printf("EVEN");
		
	}
	
	return 0;
}
