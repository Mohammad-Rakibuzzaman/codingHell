#


# def my_function_with_args(username, greetings):
#     print("Hello, %s, From my Function! %s !!!!!" % (username, greetings))


# my_function_with_args("Ratul", "Welcome*")


# Functions may return a value to the caller, using the keyword- 'return' . For example:
# def sum_two_numbers(a, b):
#     return a + b


# print(sum_two_numbers(2, 6))


# # Define our 3 functions
# def my_function():
#     print("Hello From My Function!")


# def my_function_with_args(username, greeting):
#     print("Hello, %s, From My Function!, I wish you %s" % (username, greeting))


# def sum_two_numbers(a, b):
#     return a + b


# # print(a simple greeting)
# my_function()

# # prints - "Hello, John Doe, From My Function!, I wish you a great year!"
# my_function_with_args("John Doe", "a great year!")

# # after this line x will hold the value 3!
# x = sum_two_numbers(1, 2)
# print(x)


###### Excercise #############
# Modify this function to return a list of strings as defined above
# def list_benefits():
#     return [
#         "More organized code",
#         "More readable code",
#         "Easier code reuse",
#         "Allowing programmers to share and connect code together",
#     ]


# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     return "%s is a benefit of functions!" % benefit


# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))


# name_the_benefits_of_functions()


# def fib(n):  # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b


# # Now call the function we just defined:
# fib(2000)
# fib


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result += [a]  # see below
        a, b = b, a + b
    return result


f100 = fib2(2000)  # call it
print(f100)


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


f100 = fib2(100)  # call it
f100
