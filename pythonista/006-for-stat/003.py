'''

Your monthly expense list (from Jan to May) looks like this,

expense_list = [2340, 2500, 2100, 3100, 2980]

Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. 
If expense is not found then it should print that as well.

'''

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]

userInput = input("Enter an expense amount: ")
userInput = int(userInput)

countPos = -1

for i in range(len(expense_list)):
    # print(i)
    if expense_list[i] == userInput:
            countPos = i
            break
    
if countPos == -1: 
      print("Not Found")
else: 
      print(f"So expense amount {userInput} occured in {month_list[countPos]}")
    
        


    
        