'''List  [1,2,3]
- General Purpose
- Most widely used data structure
- Grow and shrink as needed
- Sequence type
- Sortable'''

# [start:end+1:step]

x = [2, 5, 8, 12, 12]

print(sum(x[-2:]))  # sums last 2 items

# sorted returns a new list without changing original

print(x.count(12))  # returns count of the number 12

print(x.index(8))  # returns the index number of an item

my_list = [i for i in range(11)]
print(my_list)

squares = [i ** 2 for i in range(10) if i > 4]

print(squares)

#######################################################

a = [3, 2, 1]
b = [4, 5]

a.extend(b)
print(a)

a.pop()  # pops last element
print(a)

a.remove(3)  # removes the number 3
print(a)

a.sort()  # this is an INPLACE sort, unlilke sorted() function

print(a)
