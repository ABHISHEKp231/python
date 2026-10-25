# condition statement if stateme
time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")
# else
time = 18  # 6 PM
if time == 20:
    print("It's time for dinner!")
else:
    print("It's not dinner time yet.")
# The elif Statement
time = 15  # 3 PM

if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not a meal time.")
# Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.
age=int(input("Enter the age of the person: "))
if age<5:
    print("The bus pass is free.")
elif age>=60:
    print("The person get citizen discount.")
else:
    print("They pay full of price.")
