
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data                           
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
i = 0
for row in data_list[1:21]:
	i+=1
	print("\tRow {0}: {1}".format(i,row))
# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")
i = 0
for row in data_list[1:21]:
            i+=1      
            print("\tGender in Row {0}: {1}".format(i, row[6]))

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
"""
Receive a list and returns a list containing the data on column indexed by parameter.

Args:
data: chicago.csv dataset
index: column index 
Returns: List of values in column specified by index

"""
def column_to_list(data, index):
   
    column_list = []
    for x in data:
            column_list.append(x[index])
    return column_list
	
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(len(data_list))
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
for i in data_list:
	if i[6].lower() == 'male':
		male+=1
	if i[6].lower() == 'female':
		female+=1	


# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
"""
Receive a list and returns a list of two positions containing in first position the quantity of tuples with info of males and the second the quantity of tuples with info of females.
Args:
data_list: chicago.csv dataset
Returns: A list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)

"""
def count_gender(data_list):

        cmale = 0
        cfemale = 0
        for i in data_list:        
                if i[6].lower() == 'male':
                         cmale+=1
                if i[6].lower() == 'female':
                        cfemale+=1                
        return [cmale, cfemale]

print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
"""
Receive a list and returns the most popular gender.
Args:
data_list: chicago.csv dataset
Returns: The most popular gender

"""
def most_popular_gender(data_list):

    if count_gender(data_list)[0] == count_gender(data_list)[1]:
       return "Equal"                                 
    if count_gender(data_list)[0] > count_gender(data_list)[1]:
       return "Male"
    else:
        return "Female"     


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")
quant = []
types = list(set([x[5] for x in data_list]))
for _type in types:
        qt = 0
        for y in data_list:        
            if y[5] == _type:
                    qt += 1
        quant.append(qt)
                               
y_pos = list(range(len(types)))
plt.bar(y_pos, quant)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Beacause there are tuples that doesn't contains Gender info."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = [float(x) for x in column_to_list(data_list, 2)] 
"""
The column data(trip_duration_list) was converted to Float because the data was in string format.
Receive a list of the trip durations and it's used a mergesort algorithm to order the list, finally is set the position of the minor and bigger duration from list and is
made a loop to know the quantity of elements from list and get the mean and median.
Args:
trip_duration_list: It's a column where are the trip duration. 
Returns: Min and Max were setted the position after ordered and mean and median was made a loop to know the quantity of elements from list and get the mean and median.

"""
def mergeSort(trip_duration_list):
    if len(trip_duration_list)>1:
        mid = len(trip_duration_list)//2
        left = trip_duration_list[:mid]
        right = trip_duration_list[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                trip_duration_list[k]=left[i]
                i=i+1
            else:
                trip_duration_list[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            trip_duration_list[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            trip_duration_list[k]=right[j]
            j=j+1
            k=k+1
            
mergeSort(trip_duration_list)
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
values = 0
for i in trip_duration_list:        
    values += i
mean_trip = values/len(trip_duration_list)
median_trip = trip_duration_list[int(len(trip_duration_list)/2)]    

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
column = column_to_list(data_list,3)
user_types = set(column)

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
param1: The first parameter.
param2: The second parameter.
Returns:
List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
