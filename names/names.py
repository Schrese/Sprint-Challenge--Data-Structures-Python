import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# create a bst from txt file 2 ===> correction... create a new bst using name that doesn't exist in either
searching2 = BSTNode('my_name')
# add each element in txt file 2 to the new node
# iterate through txt file
for n2 in names_2:
    # add each element to bst
    searching2.insert(n2)

for name in names_1:
    if searching2.contains(name):
        duplicates.append(name)
    # else:
    #     return

########## DON'T NEED BELOW
# create a bst from txt file 1 ===> correction... create a new bst using name that doesn't exist in either
searching1 = BSTNode('my_other_name')
# iterate through txt file
for n1 in names_1:
    # add each element to bst
    searching1.insert(n1)

# for n2 in searching2:
#     for n1 in searching1:
#         if n1 == n2:
#             duplicates.append(n1)
###### I JUST REALIZED I DON'T NEED ANOTHER BST

# compare the first bst to the second one
    # for each element in the first binary tree
    # if it matches another element in the second binary search tree
    # add that element to the duplicates list






# Before I begin:
# I need to bring in my binary search tree file from previous days
# after that
# create a binary search tree from one of the txt files
# Then
# create another binary search tree from the other txt file
# search through 2nd search tree to find the common names
# add those names to the list

# Questions: 
# I'm not sure if I need to do this twice (ie. I'm not sure if I need to have one function that looks like the first one and then try stretch or if it's something else)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
