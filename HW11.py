#Name:  Helber Diaz Vasquez
#Class: 5th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
var1 = random.randint(1, 100)
var2 = random.randint(1, 100)
var3 = random.randint(1, 100)
num_list = [var1, var2, var3]

#3. Print the list.
print(num_list)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if var1 >= var2 and var1 >= var3:
    highest = var1
elif var2 >= var1 and var2 >= var3:
    highest = var2
else:
    highest = var3
#5. Tie the result (the largest number) from #4 to a variable called "num".
num = highest
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("The number is divisible by both 2 and 3.")
    else:
        print("The number is divisible by 2.")
else:
    if num % 3 == 0:
        print("The number is divisible by 3.")
    else:
        print("The number is divisible by neither 2 nor 3.")