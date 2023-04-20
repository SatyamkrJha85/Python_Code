# wap a program to print multiplication table of a given no using for loop
''' a=int(input("enter a number"))
for i in range(1,11):
    print(str(a)+"X"+str(i)+"="+str(i*a))
'''
'''
    # Q2 same problem solve using while loop
i=1
no=int(input("enter your table no "))
while i<11:
    print(i,"X",no,"=",no*i)
    i=i+1
 # Q3 wap to greet all the person name start with s

names=["satyam","sohan","saurabh","suresh","kavya"]
for name in names:
    if name.startswith("sa"):
        print("hello",name)
        '''

# Q4 wap to find wheather a given number is prime or not

 # no=int(input("enter your no "))
'''
prime=True
for i in range(2,no):
         if(no%i==0):
             prime=False
             break
if prime:
  print("no is prime ")
else:print("no is not prime")'''

# Sum of first n natural no using while loop 5=5+4+3+2+1=15
'''i=0
while no>0:
    i=i+no
    no=no-1
    print(i)

# wap to calculate the factorial of a given number using for loop.
fact=1
for i in range(1,no+1):
    fact=fact*i
    print(fact)


# print this simple pattern
n=4
for i in range(5):
  print("*"*(i))
  
*
**
***
****
*****
n=5
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()

*****
****
***
**
*
for k in range(5,0,-1):
    for d in range(1,k+1):
        print("*",end="")
    print()


'''









'''
      *
     * *
    * * *
   * * * *  
for i in range(1,6):
    for j in range(1,6-i):
         print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()'''

'''
   * * * * * *
    * * * *
     * * *
      * *
       *
for q in range(6,0,-1):
    for k in range(0,6-q):
     print(" ",end="")
    for j in range(1,q+1):
          print("*",end=" ")
    print()
     '''

# print a reverse multiplication table:
a=int(input("enter your no "))
for i in range(10,0,-1):
    print(a,"X",i,"=",a*i)
