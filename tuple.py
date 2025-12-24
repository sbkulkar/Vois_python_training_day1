





























t = (10, 20, 30, 20, 40, 50)

# 1. Maximum and Minimum elements in a tuple
maxi = t[0]
mini = t[0]

for i in t:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print("Tuple:", t)
print("Maximum:", maxi)
print("Minimum:", mini)

# 2. Convert list of tuples into dictionary
l_o_t= [("a", 1), ("b", 2), ("c", 3)]
d = {}

for k, val in l_o_t:
    d[k] = val

print("Dictionary:", d)

# 3. Count occurrence of an element without built-in method
element = 20
count = 0

for i in t:
    if i == element:
        count += 1

print("Occurrence of", element, ":", count)

# 4. Tuple with mutable elements and modify them
mutable_tuple = ([1, 2, 3], [4, 5])
print("Before modification:", mutable_tuple)

mutable_tuple[0][0] = 99

print("After modification:", mutable_tuple)

# 5. Swap two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)

print("Before swap:")
print("t1 =", t1)
print("t2 =", t2)

t1, t2 = t2, t1

print("After swap:")
print("t1 =", t1)
print("t2 =", t2)















