'''Tuple (R,)
- Immutable
- Useful for fixed data
- Faster than lists
- Sequence type'''

x = 2,  # parenthesis are optional
y = (1, 2, 3)
print(type(x))

my_list = [2, 4, 6]
my_tuple = tuple(my_list)
print(my_tuple)

#del (my_tuple[1])  # TypeError: 'tuple' object doesn't support item deletion

z = ([100, 200], 300)  # because list are mutable, we can change list
del (z[0][0])  # removes the 100
print(z)
