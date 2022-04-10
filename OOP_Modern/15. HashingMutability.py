import gc

# Can be compared to other object
# If equals, shares same hash with other object
# hash key immutable


name_str = "Andy"

print(id(name_str))

name_str = "AndyB"

print(id(name_str))
