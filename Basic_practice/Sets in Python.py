# Set is a colletion of non repeating element:
# Important: This syntax will create an empty dictionary and not an empty set
a={}
print(type(a))

# An empty set can be created using the below syntax:
b=set()
print(type(b))

# for declearing set (set not repeat same item)
c={3,4,2,4,5,3}
print(c)
d={6,7,3,1,9}
print(d)

# for adding item use b.add(item):
# for remove a specific item use d.remove(item)

d.add(34)
d.add(32)
print(d)
d.remove(34)
print(d)

# Pop function remo
print(d.pop())
print(d.pop())
print(d.pop())

# Union and intersection function
e={4,5,3,2}
f={5,6,4,3}
print(e.union(f))
print(e.intersection(f))
