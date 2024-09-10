'''
Create variables to store the lengths of three sides of a triangle. 
Calculate and store the perimeter and area of the triangle in new variables. 
Print the results.

'''
import math

a = 10
b = 20
c = 15

pm = a + b + c
s = pm / 2
ar = math.sqrt(s * (s-a) * (s-b) * (s-c))

print("so the total Perimeter of the triangle is %0.2f and area is %0.2f" %(pm, ar))
