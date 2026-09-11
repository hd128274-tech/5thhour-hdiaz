#Name: Helber Diaz
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
List1=[2,3,5,6,7,6,3,4,5,]

#2. Sort the list from highest to lowest.
List1. sort()
#3. Create an empty list.
List2=[]
#4. Remove the median number from the first list and add it to the second list.
List2.append(List1[4])
#5. Remove the first number from the first list and add it to the second list.
List2.append(List1[0])

#6. Print both lists.
print(List2)
print(List1)
#7. Add the two numbers in the second list together and print the result.
bar1=List2[0]+List2[1]
print(bar1)
#8. Add the sum from #7 to the first list.
List1.append(bar1)
#9. Sort the first list from lowest to highest and print it
List1. sort()
print(List1)