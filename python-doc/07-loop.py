##FOR

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)


### WHILE
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


0 % 2

####### break########

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


#####continue######

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


# Prints out 0,1,2,3,4 and then it prints "count value reached 5"


# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

# Prints out 1,2,3,4
for i in range(4, 20):
    if i % 5 == 0:
        break
    print(i)
else:
    print(
        "this is not printed because for loop is terminated because of break but not due to fail in condition"
    )

5 % 5


"""
Can we use "else" clause for loops?
Unlike languages like C,CPP.. we can use else for loops. When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If a break statement is executed inside the for loop then the "else" part is skipped. Note that the "else" part is executed even if there is a continue statement.


"""
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

# Prints out 1,2,3,4
for i in range(1, 5):
    if i % 5 == 0:
        break
    print(i)
else:
    print(
        "this is not printed because for loop is terminated because of break but not due to fail in condition"
    )


for i in range(1, 5):  # This loop only runs once, with i = 1
    if i % 5 == 0:
        break
    print(i)
else:
    print("This is not printed...")


for i in range(1, 7):  # This loop only runs once, with i = 1
    if i % 5 == 0:
        break
    print(i)
else:
    print("This is not printed...")


"""
Summary:
If the loop finishes naturally (without hitting break), the else block executes.
If the loop exits due to a break, the else block is skipped.


"""


numbers = [
    951,
    402,
    984,
    651,
    360,
    69,
    408,
    319,
    601,
    485,
    980,
    507,
    725,
    547,
    544,
    615,
    83,
    165,
    141,
    501,
    263,
    617,
    865,
    575,
    219,
    390,
    984,
    592,
    236,
    105,
    942,
    941,
    386,
    462,
    47,
    418,
    907,
    344,
    236,
    375,
    823,
    566,
    597,
    978,
    328,
    615,
    953,
    345,
    399,
    162,
    758,
    219,
    918,
    237,
    412,
    566,
    826,
    248,
    866,
    950,
    626,
    949,
    687,
    217,
    815,
    67,
    104,
    58,
    512,
    24,
    892,
    894,
    767,
    553,
    81,
    379,
    843,
    831,
    445,
    742,
    717,
    958,
    609,
    842,
    451,
    688,
    753,
    854,
    685,
    93,
    857,
    440,
    380,
    126,
    721,
    328,
    753,
    470,
    743,
    527,
]

# len(numbers)
for number in numbers:
    if number % 2 == 0:

        print(number)

        if number == 237:
            break
