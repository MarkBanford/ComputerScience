class MercedezBenz:
    doors = 2
    wheels = 4


# class state is stored in a mapping-proxy object and retrieved using __dict__

print(MercedezBenz.__dict__)

MercedezBenz.doors = 4
print(MercedezBenz.__dict__)

MercedezBenz.model = 'G'
print(MercedezBenz.__dict__)  # property binding

m3 = MercedezBenz()  # class state shared by all instances
m4 = MercedezBenz()

print(m3.doors)
print(m4.model)
