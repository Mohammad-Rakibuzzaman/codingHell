# Boolean operators

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# The "in" operator

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


statement = False
another_statement = True
if statement is True:
    # do something
    print("one pience")
elif another_statement is True:  # else if
    # do something else
    print("Berserk")
else:
    # do another thing
    print("tv series")

"""
The 'is' operator
Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:
"""
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False


"""
The "not" operator
Using "not" before a boolean expression inverts it:

"""

print(not False)  # Prints out True
print((not False) == (False))  # Prints out False


# change this code
number = 16
second_number = None or 0
first_array = [1, 1, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")


# if not second_number:
#     print("6")

a = 2
b = 2
if a == b:
    print("a is equal to b")


#### How do you use a ternary operator?

name = "John"
result = name == "John" ? "John" : "Jane"

print(result)