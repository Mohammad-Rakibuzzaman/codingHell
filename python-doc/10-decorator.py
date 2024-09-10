# def my_decorator(func):
#     def wrapper():
#         print("Before the function.")
#         result = func()  # Call the original function
#         print("After the function.")
#         return result  # Ensure the result of func() is returned

#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")  # Print "Hello!" inside the function


# # Call the function
# say_hello()


def my_decorator(func):
    print("Before the function.")
    result = func()  # Call the original function
    print("After the function.")
    return result  # Ensure the result of func() is returned


@my_decorator
def say_hello():
    print("Hello!")  # Print "Hello!" inside the function


# Call the function
say_hello()
