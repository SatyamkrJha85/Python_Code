# wap a program to create a dictionary of hindi words with value as their english
# translation provide user with an option to look it up!
'''
mydict={
    "kitab":"book","panna":"notebook","diwal":"wall"
}
print("option are : ",mydict.keys())
a=input("enter the Hindi word\n")
print("the meaning of your word is :",mydict[a])

# wap to input eight numbers form the user and display all the unique number  add
n1=input("enter your number")
n2=input("enter your number")
n3=input("enter your number")
n4=input("enter your number")
n5=input("enter your number")
n6=input("enter your number")
n7=input("enter your number")
numbers={n1,n2,n3,n4,n5,n6,n7}
print(numbers) '''

# can we have a set with 18(int) and "18"(str) as a value it
a=(3,"3")
print(a)

# what will be the length of following set s
s=set()
s.add(34)
s.add(34.0)
s.add("34")
print(len(s))

# s={ } what is the type of s
s={}
print(type(s))

# Create an empty dictonary allow 4 friends to enter their favourite language as value and use keys as
# their names assume that the names are unique

t={ }
d=input("enter your language ")
k=input("enter your language ")
e=input("enter your language ")
f=input("enter your language ")
t['subham']=d
t['sangita']=k
t['satya']=e
t['sandhya']=f
print(t)

# Q :If name of 2 friends are same what will happen to the program in problem 6:
 #Ans : (problem is old name is removed and print only latest name: )

 # Q: if language of two friends are same what will happen to the program in problem 6:
 # Ans: nothing change


 # Q : can you change the value inside a list which is contained in set 5 s={8,7,12,"harry",[1,2]}
# no change