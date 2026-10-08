#Name:Helber Diaz Vasquez
#Class: 5th Hour
#Assignment: HW10
import random

#1. Print "Hello World!"
print("Hello world")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
A = random.randint(1, 10)
B = random.randint(1, 10)
C = random.randint(1, 10)


#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if A > 5:
    print("Variable A is greater than 5.")
elif A < 5:
    print("Variable A is less than 5.")
else:
    print("Variable A is equal to 5.")


#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if 3 <= B <= 7:
    print("Variable B is between 3 and 7.")
else:
    print("Variable B is not between 3 and 7.")

#6. Make an if statement that prints if variable C is even or odd.
if C % 2 == 0:
    print("Variable C is even.")
else:
    print("Variable C is odd.")

#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
variable_seven = 3 + random.randint(1, 20)

#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
sum_ABC = A + B + C

if variable_seven > sum_ABC:
    print(f"The variable from #7 ({variable_seven}) is greater than A + B + C ({sum_ABC}).")
elif variable_seven < sum_ABC:
    print(f"The variable from #7 ({variable_seven}) is less than A + B + C ({sum_ABC}).")
else:
    print(f"The variable from #7 ({variable_seven}) is equal to A + B + C ({sum_ABC}).")