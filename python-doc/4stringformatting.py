# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
# This prints out "John is 23 years old."
name = "John"
age = 23
height = 5.521
print("%s is %d years old. and his height is %0.2f." % (name, age, height))


#### Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string. For example:


# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)


"""
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
"""

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(
    "%s %s %s. Your current balance is $%s."
    % (format_string, data[0], data[1], data[2])
)

###########solved#################
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)


if "substring".startswith("sub"):
    print("substring starts with sub")


# The correct way to join a list of strings with a comma delimiter in Python is:

print(",".join(["foo", "bar"]))


list = ["rat", 25]
# list = ",".join(["foo", "bar"])
for _ in list:
    print(_, end="")


print("foo,bar,rat".split(","))


print(" ".join([x.capitalize() for x in "yo yo yo".split()]))


"this is fun".find("fun")

