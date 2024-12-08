'''
Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.

    Ask user to enter his fasting sugar level
    If it is below 80 to 100 range then print that sugar is low
    If it is above 100 then print that it is high otherwise print that it is normal


'''


sugerLevel = int(input("Please Enter your fasting sugar level: "))

if(sugerLevel < 80):
    print("Sugar is low")
elif(sugerLevel > 100):
    print("It is high.")
else:
    print("It is normal.")
