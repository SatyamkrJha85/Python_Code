'''
i=1
while i<51:
    print(i)
    i=i+1
'''
'''
# Quick Question :- wap to print the content of a list using while loops
fruits=['mango','apple','blackberry','orange']
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1

    satyam=["satya",3344,"mohan",34.3]
    a=0
    while a<len(satyam):
        print(satyam[a])
        a=a+1

        # For loop
    for item in satyam:
        print("item is:",item)
  # Range function
for s in range(23):
      print("range is",s)

      # Range function for specific items
for r in range(3,5):
          print("Function is : ",r)

         # Range in step size(ex 2 is a step size 2 jump direct two number
for k in range(3,10,2):
             print(k)

             # for with loop
for b in range(1,4):
    print(b)
else: print("this is inside else of for loop")


# Break statement
for n in range(4,9):
    print(n)
    if(n==5):
        break

 # Continue function
for w in range(12):
     if w==5:
         continue
         print("the value is ",w)
         '''
         # Pass function use of pass is skip the loop
h=89
if h>234:
 pass
print("hey buddy")

while 89<34:
    pass
print("allright")