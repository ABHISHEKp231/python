
   
n = int(input("Enter num: "))
l = [int(num) for num in input("Enter num: ").split()]
print('sum:', sum(l))
print('max:', max(l))
print('min:', min(l))
l.reverse()
print('reverse:', l)
#Sum of Prices:

#Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.
prices = {"apple": 1, "banana": 3, "orange": 4, "grape": 2, "kiwi": 1}
total=0
for item,price in prices.items():
    total+=price
print("Total price of all items:", total)
l=[1,2,3,45,6,7,8,9,10]
l=[x*2 for x in l]
print(l)