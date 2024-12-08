'''

    After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads

'''

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

count = 0
tailCount = 0
i = 0
for i in range(len(result)):
    if(result[i] == "heads"):
        count += 1
    else:
        tailCount += 1
        

print(count)
print(tailCount)

