print("Hello")

print("Hello", "World")

print("Hello", "World", sep="***")

print("Hello", "World", end="***")

print("Hello", end="***")
print("World")

name = "dip"
age = 32
print(name, "is", age, "years old.")


print("%s is %d years old." % (name, age))

price = 150
item = "apple"
print("The %s costs %10d cents per kg" % (item, price))

print("The %+10s costs %5.3f cents" % (item, price))

print("The %+10s costs %10.2f cents" % (item, price))

item_dict = {"item": "banana", "cost": 24}
print("The %(item)+10s costs %(cost)7.1f cents" % item_dict)


txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
# numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John", 36)
# empty placeholders:
txt3 = "My name is {}, I'm {}".format("John", 36)

print(txt1)
print(txt2)
print(txt3)


num1, num2, num3 = map(int, input("Enter three numbers separated by spaces: ").split())


print(f"First number: {num1}, Second number: {num2}, Third number: {num3}")

print(type(num1))
