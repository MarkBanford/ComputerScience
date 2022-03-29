'''Set {1,2,3}
- Store non-duplicate items
- Very fast compared to lists
- Math set operations (union, intersect)
- Unordered'''

x = {3, 5, 3, 5}  # {5, 3}   removes duplicates

my_set = {i for i in range(101)}

my_set.pop()  # pops first item from the set

set1 = {i for i in range(50) if i % 2 == 0}
set2 = {i for i in range(50)if i % 2 == 1}

print(set1)
print(set2)
print(set1 ^ set2)
