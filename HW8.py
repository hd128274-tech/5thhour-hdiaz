#Name: Helber Diaz Vasquez
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
from ctypes import LibraryLoader

#2. print "Hello World!"
print("hello worrld")
#3. Create three different variables that each randomly generate an integer between 1 and 10
var1=random.randint(1,10)
var2= random.randint(1,10)
var3= random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(var1,var2,var3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
var1=var1+2
var2=var2-4
var3=var3*1.5
#6. Print each result from #5 on the same line.
print(var1,var2,var3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6

List1=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
List1.sort()
print(List1)

#9. Add together the highest three numbers in the list from #7 and print the result.
var4=List1[1]+List1[2]+List1[3]
print(var4)
#10. Create a list with 5 names of other students in this class and print the list.
List2= ["HELBER", "ANTONY", "GAVIN", "SANTY", "ETHAN"]
print(List2)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(List2)
print(List2)
#12. Print a random choice from the list of names from #10.

print(random.choice(List2))



