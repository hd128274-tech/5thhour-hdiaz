#Name:Helber Diaz Vasquez
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library
import "random"
#2. print "Hello World!"
print("Hello World")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
print("--- Steps 3 & 4 ---")
a = int(input("Enter an integer for a: "))
b = int(input("Enter an integer for b: "))
c = int(input("Enter a non-zero integer for c: "))

# Add a and b, then divide by c
result = (a + b) / c
print(f"({a} + {b}) / {c} = {result}")
#4. Add a and b together, then divide the sum by c. Print the result.
print(result)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print("\n--- Step 5 ---")
# Standard rounding to the nearest whole integer
if result - 'math'.floor(result) < 0.5:
    rounded_result = 'math'.floor(result)
else:
    rounded_result = 'math'.ceil(result)

# Determine if the rounded result is even or odd
if rounded_result % 2 == 0:
    parity = "even"
else:
    parity = "odd"

print(f"Rounded result: {rounded_result} (which is {parity})")
#6. Create a list of five different random integers between 1 and 10.
rint("\n--- Steps 6 to 9 ---")
# #6. Create a list of 5 random integers between 1 and 10
random_list = ['random'.randint(1, 10) for _ in range(5)]
print(f"Initial random list: {random_list}"
#7. Print the 4th number in the list.
print(f"The 4th number in the list is: {random_list[3]}")
#8. Append another integer to the end of the list, also random from 1 to 10.
random_list.append('random'.randint(1, 10))
print(f"List after appending a 6th number: {random_list}")
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
random_list.sort()
print(f"Sorted list: {random_list}")
print(f"The 4th number in the sorted list is: {random_list[3]}")

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
print("\n--- Step 10 ---")
i = 1
while i <= 100:
    print(f"i is currently: {i}")
    i += i  # Adds i to itself (doubles it each iteration)
#11. Create a list containing the names of five other students in the classroom.
print("\n--- Steps 11 & 12 ---")
# #11. List of five student names
students = ["Alex", "Blake", "Charlie", "Dylan", "Emerson"]
#12. Create a for loop that individually prints out the names of each student in the list.
for student in students:
    print(f"Student Name: {student}")

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
print("\n--- Step 13 ---")
for count in range(1, 101):
    print(count)
    # Check if the number is a multiple of 10 to end early
    if count % 10 == 0:
        print(f"Ending loop early because {count} is a multiple of 10.")
        break
#14. Free space. Do something creative. :)
print("\n--- Step 14: Creative Space ---")
import time

print("Initializing digital code sequence...")
time.sleep(0.5)

symbols = ["0", "1", " ", "x", "%", "$", "#", "@"]
for _ in range(15):
    # Create a random flowing line of matrix-like code strings
    line = "".join('random'.choice(symbols) for _ in range(40))
    print(line)
    time.sleep(0.1)

print("\nProcess Complete. Code execution successful! 🚀")