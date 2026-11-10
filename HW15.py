#Name:HERlber Diaz Vasquez
#Class: 5th Hour
#Assignment: HW15


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
print("Hello World")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for i in range(1, 31):
    if i % 2 == 0:
        print(i)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)
#4. Create a for loop that prints 5 different animals from a list.
animals = ["Lion", "Elephant", "Penguin", "Koala", "Dolphin"]

for animal in animals:
    print(animal)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
word = input("Enter a word: ")

# Reverse the string and loop through it
for letter in word[::-1]:
    print(letter)
#6. Create a list containing 10 integers of your choice and print the list.
numbers = [14, 22, 7, 45, 90, 33, 18, 5, 62, 11]
print(numbers)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0

# Task 8: Loop and count
for num in numbers:
    if num % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

print("Even numbers:", evenNumbers)
print("Odd numbers:", oddNumbers)
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.



#9. Create a variable that asks the user for an integer and an empty integer variable.
user_num = int(input("Enter an integer: "))
factorial = 1

# Task 10: Loop to find the factorial
for i in range(1, user_num + 1):
    factorial *= i

print(f"The factorial of {user_num} is: {factorial}")
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)rint(f"The factorial of {user_num} is: {factorial}")