'''
You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
Find out using python, how many dollars is the shopkeeper going to give you back?
'''
#solution
'''
totalCost = 9 x 1.49

20-totalCost

'''

givnMoney = 20
totalCost = 9 * 1.49
print(totalCost)
print("Shopkeeper going to give back is {:.2f}".format(givnMoney-totalCost))
