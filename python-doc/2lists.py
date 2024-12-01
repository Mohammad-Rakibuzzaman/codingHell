# ur_list = []

# ur_list.append(2)
# ur_list.append(1)
# ur_list.append(12)

# print(ur_list[2])

# for _ in ur_list:
#     print(_)


numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
strings.append("hello")
strings.append("world")
numbers.append(1)
numbers.append(2)
numbers.append(3)

# this code should write out the filled arrays and the second name in the names list (Eric).
for x in numbers:
    print(x)
print(strings)
print("The second name on the names list is %s" % second_name)

numbers.pop()  # will remove last element

del numbers[0]  # to remove first elemenet
numbers.pop(0)  # to remove first elemenet

# to chekkc if an item not in the list
my_list = [1, 2, 3, 4, 5]
item = 6

if item not in my_list:
    print(f"{item} is not in the list.")
else:
    print(f"{item} is in the list.")
