#Name:Helber Diaz Vasquez
#Class: 5th Hour
#Assignment: HW14
from time import time

print("Hello World")
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.t("Hello World!")t("Hello World!")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
num = 1
while num <= 30:
    if num % 2 == 0:  # Modulo checks if the remainder is 0
        print(num)
    num +=1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
num =3
while num <= 30:
    if num % 3 == 0:
        num += 1   # Increment before continuing to avoid an infinite loop
        continue   # Skips the rest of the loop code and goes to the next iteration
    print(num)
    num +=1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
import random

while True:
    roll = random.randint(1, 6)
    print(roll)
    if roll == 1:
        break  # Exits the loop immediately

#5. Create a while loop that asks for a number input until the user inputs the number 0.
user_input = None

while user_input != 0:
    # We cast to int() assuming the user enters a valid number
    user_input = int(input("Enter a number (0 to quit): "))