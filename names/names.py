import time
#these are only used to be able to find files to open
import os
import sys
start_time = time.time()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def contains(self, target):
        if target == self.value:
             return True

        if target < self.value:
             if self.left:
                 return self.left.contains(target)
             else:
                 return False
        else:
             if self.right:
                 return self.right.contains(target)
             else:
                 return False

    def insert(self, value):
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)




# joining current dir to path to this file, (wouldn't run on my mac)
f = open(os.path.join(sys.path[0], 'names_1.txt'), 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(os.path.join(sys.path[0], 'names_2.txt'), 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# This runtime is O(n^2) because the nested loop 

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
    # for name_2 in names_2:
    #     if name_1 == name_2:
    #         duplicates.append(name_1)


# This runtime is O(n) because one loop
# firstNames = tuple(names_1)

# for name in names_2:
#     if name in firstNames:
#         duplicates.append(name)


#not sure if I can use a tuple so here's another solution
# this is O(2n) but simplified to O(n*log(n)) but doesn't work for some reason

bst = BSTNode(names_1[0])

for i in range(1,len(names_1)):
    bst.insert(names_1[i])

for name2 in names_2:
    if bst.contains(name2):
        duplicates.append(name2)



# This runtime is O(n) because one loop
# firstNames = tuple(names_1)

# for name in names_2:
#     if name in firstNames:
#         duplicates.append(name)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
