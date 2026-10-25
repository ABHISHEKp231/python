#for loop
for i in range(5):
    print(i, end=" ")
list=["red","green","blue"]
for color in list:
    print(color)
    #Using range() with for Loops
for i in range (1,9,2):
    print(i)
for i in range(1,11):
    print(f"3x{i}={3*i}")
#Sum of First 10 Numbers: Write a program using a for loop that calculates the sum of numbers from 1 to 10.python with ou
total_sum = 0
for num in range(1, 11):
    total_sum += num  
print("The sum of numbers from 1 to 10 is:", total_sum)