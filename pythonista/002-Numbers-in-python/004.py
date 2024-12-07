# Print binary representation of number 17

'''


'''

num = 17

print("Binary of the given number is: ", format(num, 'b'))
    
#Use "b" to convert the number into binary format:
num = 4
txt = "The binary version of {0} is {0:b}"

print(txt.format(num))


#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))
