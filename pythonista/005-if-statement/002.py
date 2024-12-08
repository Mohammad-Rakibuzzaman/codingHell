'''
2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print
 "They don't belong to same country"

'''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

x, y = input("Enter 2 cities: ").split()

if(x in india and y in india):
    print("Both cities are in India.")
elif(x in pakistan and y in pakistan):
    print("Both cities are in Pakistan.")
elif(x in bangladesh and y in bangladesh):
    print("Both cities are in Bangladesh.")
else:
    print("They don't belong to same country")