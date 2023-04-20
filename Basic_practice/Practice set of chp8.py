# wap to find greater no using function
def find(a,b,c):
    if(a>b or a>c  ):
        print("a is a greater no ",a)
    elif(b>a or b>c):
        print("b is greater no ",b)
    elif(c>a or c>b):
        print("C is greater no ",c)
    else:print("nothing")

print(find(45787855,2,45))



# write a python program using function to convert calsius to fahrenhite
def farh(cel):
    return (cel *(9/5))+32

print("your fagreheit Tempreture is ",farh(67))



# how do you present a python print() function to print a new line of the end

print("Show",end=" ")
print("Me ",end=" ")
print("perfect", end=" ")
print("youtube",end=" \n")



# wap a recursive function to print n natural no 5+4+3+2+1=15
def natural(no):
    if(no==1):
        return 1
    return no+natural(no-1)


print("The ans is ",natural(5))

'''
# wap to print pattern using function
def pattern(n):
   for i in range(n):
    print("*" * (n-i))

    pattern(5)'''


# wap to remove a given world from a list and setup it at a same time
def lisa(d,word):
 newstr=d.replace(word,"")
 return newstr.strip()


d="  satyam subham sanhay  "
n=lisa(d,"satyam")
print(n)