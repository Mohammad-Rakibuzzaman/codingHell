'''

    Lets say you are running a 5 km race. Write a program that,
        Upon completing each 1 km asks you "are you tired?"
        If you reply "yes" then it should break and print "you didn't finish the race"
        If you reply "no" then it should continue and ask "are you tired" on every km
        If you finish all 5 km then it should print congratulations message

'''

# finOrNot = -1

# for i in range(1, 6):
#     x = input("Are you tired?: ")
#     if(x == "yes"):
#         print("you didn't finish the race")
#         break
#     else:
#         finOrNot += 1

# if(finOrNot > 0):
#     print("congratulations. you have finished it!")
        
        
        
    
print("\nExercise 4\n")

for i in range(5):
    print(f"You ran {i+1} miles") # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")




