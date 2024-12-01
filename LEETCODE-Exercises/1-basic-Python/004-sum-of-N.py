takeNumber = int(input())

# count = 0
# i = 1
# while i <= takeNumber:
#     count += i
#     i += 1
# print(count)

count = 0

for i in range(takeNumber + 1):
    count += i
    print(i)
print(count)
