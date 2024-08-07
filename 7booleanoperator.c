#include <stdio.h>

int main() {
	// your code goes here
	
	int firstNum, secNum;
	
	scanf("%d %d", &firstNum, &secNum);
	printf("isEqual: %d\nisNotEqual: %d\nisGreaterThan: %d\nisLesserThan: %d\nisGreaterThanEqualTo: %d\nisLesserThanEqualTo: %d", firstNum == secNum, firstNum != secNum, firstNum > secNum, firstNum < secNum, firstNum >= secNum, firstNum <= secNum);
	
	
	return 0;
}
