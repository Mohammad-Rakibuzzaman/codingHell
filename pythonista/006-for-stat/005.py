'''
Write a program that prints following shape

*
**
***
****
*****

'''


# for i in range(1, 6):
#     print(i * "*")


### codebasis solution

for i in range(1, 6):
    starCol = ''
    for j in range(i):
        starCol += "*"
    print(starCol, f" Oh yeah")