#Name: Helber Diaz Vasquez
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
neely_car_dictionary = {
"brand": "Mini",
"model": "Honda civic",
"year": [20,21,22]}



#3. Print the keys of the dictionary from #2.
print(neely_car_dictionary)
#4. Print the values of the dictionary from #2
print("Model"),
#5. Print one of the three numbers from the list by itself

print(neely_car_dictionary["model"])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
neely_car_dictionary = {"passing": True}
#7. Print the entire dictionary from #2 with the updated key and value.
print(neely_car_dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
classmates = {
    "student1": {"name": "Sarah", "major": "Computer Science", "gpa": 3.8},
    "student2": {"name": "Michael", "major": "Mathematics", "gpa": 3.9},
    "student3": {"name": "Emily", "major": "Physics", "gpa": 3.7}
}
#9. Print the names of all three classmates on the same line.
print(classmates["student1" ["Sarah","Michael","Mathematics"]])
print(classmates["student2" ["Michael","Mathematics"]])
print(classmates["student3" ["Mathematics"]])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictioary from #8.
neely_car_dictionary = {
"brand": "Mini",
"model": "Honda civic",
"year": [20,21,22]}
