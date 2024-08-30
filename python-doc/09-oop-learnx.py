class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


# We'll explain why you have to include that "self" as a parameter a little bit later. First, to assign the above class(template) to an object you would do the following:


class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
myobjectx.variable

print(myobjectx.function)


############################################


class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()

print(myobjectx.variable)


#######################################


class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Print out both values
print(myobjectx.variable)  # Outputs: blah
print(myobjecty.variable)  # Outputs: yackity

# Corrected function call
myobjectx.function()  # Outputs: This is a message inside the class.


#####################################################
class MyClass:
    variable = "blah"

    def get_message(self):
        return "This is a message inside the class."


myobjectx = MyClass()
print(myobjectx.get_message())  # Outputs: This is a message inside the class.


####init()
# The __init__() function, is a special function that is called when the class is being initiated. It's used for assigning values in a class.
class NumberHolder:

    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number


var = NumberHolder(7)
print(var.returnNumber())  # Prints '7'
