givenYear = int(input())

if givenYear > 0:
    if givenYear % 4 == 0 and (givenYear % 100 != 0 or givenYear % 400 == 0):
        print(givenYear, " is Leap year")
    else:
        print("Not leap year")
else:
    print("Invalid year")


# year = int(input("enter the year "))

# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print(year, "is a leap year")
#         else:
#             print(year, "is not a leap year")

#     else:
#         print(year, "is leap year")

# else:
#     print(year, "is not leap year")


# year = 1900
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
