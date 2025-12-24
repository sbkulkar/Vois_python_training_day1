# Predefined sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set1:", set1)
print("Set2:", set2)

# 1. Union, Intersection, Difference, Symmetric Difference
print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# 2. Remove common elements from two sets
common_removed_1 = set1 - set2
common_removed_2 = set2 - set1
print("\nAfter removing common elements:")
print("Set1:", common_removed_1)
print("Set2:", common_removed_2)

# 3. Check whether one set is a subset of another
if set1.issubset(set2):
    print("\nSet1 is a subset of Set2")
else:
    print("\nSet1 is NOT a subset of Set2")

# 4. Print elements greater than a given number
num = 25
print("\nElements greater than", num, ":")
for x in set1:
    if x > num:
        print(x)

# 5. Convert list with duplicates to set and back to list
lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(lst))

print("\nOriginal list:", lst)
print("Unique list:", unique_list)
