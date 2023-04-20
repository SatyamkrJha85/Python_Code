'''
tuple1=(1,2,3,4,5,6,7,8,9)
print(tuple1)
tuple2=tuple1+(10,)
print(tuple2)
tuple3=tuple2[:11]+tuple1[::-1]
print(tuple3)

tuple1=tuple(input("enter your tuple").split())
print(tuple1[::-1])
'''

#Q5

n=int(input("Enter the total keys: "))
d={}
for i in range(0,n,1):
    k=input("Enter the key: ")
    v=int(input("Enter the values: "))
    d.update({k:v})
print("My dictionary ",d)
var=sum(d.values())
print("Sum of values",var)