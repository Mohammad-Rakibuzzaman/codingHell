'''

    Lets say you are running a 5 km race. Write a program that,
        Upon completing each 1 km asks you "are you tired?"
        If you reply "yes" then it should break and print "you didn't finish the race"
        If you reply "no" then it should continue and ask "are you tired" on every km
        If you finish all 5 km then it should print congratulations message

'''

finOrNot = 0

for i in range(1, 6):
    if(i == 1):
        x = input("Are you tired?: ")
        if(x == "yes"):
            finOrNot += 1 
            break
    


print(findOrNot)

