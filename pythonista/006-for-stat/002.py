###Print square of all numbers between 1 to 10 except even numbers


for i in range(1, 11):
    if(i%2 != 0):
        print(i**2, end=" ")
    


print("\nExercise 2 by cb\n")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)