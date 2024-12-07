'''
You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

'''

rLength = 5.5
totalArea = rLength ** 2
print(totalArea)

totalCost = totalArea * 500

print(int(totalCost))