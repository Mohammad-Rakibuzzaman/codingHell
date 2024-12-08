'''
Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print
 "They don't belong to same country"


'''


# 1. Write a program that asks user to enter a city name and it should tell which country the city belongs to


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

userPrompt = input("Please Enter the city you for finding the country name: ")

if(userPrompt in india):
    print("India")
elif(userPrompt in pakistan):
    print("Pakistan")
elif(userPrompt in bangladesh):
    print("Bangladesh")
else:
    print("Sorry invalid input.")










