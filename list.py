# 1. Create an empty list called my_list
my_list = []
print(f"Initial list: {my_list}\n")

# 2. Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending 10, 20, 30, 40: {my_list}\n")

# 3. Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print(f"After inserting 15 at index 1: {my_list}\n")

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"After extending with [50, 60, 70]: {my_list}\n")

# 5. Remove the last element from my_list
my_list.pop()
print(f"After removing the last element: {my_list}\n")

# 6. Sort my_list in ascending order
my_list.sort()
print(f"After sorting the list: {my_list}\n")

# 7. Find and print the index of the value 30 in my_list
try:
    index_of_30 = my_list.index(30)
    print(f"The index of the value 30 is: {index_of_30}")
except ValueError:
    print("The value 30 was not found in the list.")