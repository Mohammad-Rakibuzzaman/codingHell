'''
Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height

'''

def calculate_area(base, height):
    area = (1/2) * base * height
    return area

baseOfArea = int(input("Give me the base(Sq feet): "))
heightOfArea = int(input("Give me the height(Sq feet): "))

solProb = calculate_area(baseOfArea, heightOfArea)

print("So the area of your triangle is: ", solProb)
