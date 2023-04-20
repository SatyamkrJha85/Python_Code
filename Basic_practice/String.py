#multiple types of declearing a string
a="satyam's"
b='satyam"satya'
print(a)
print(b)
c='''satyam"s and Kumar '''
print(c)
d=''' Hello user"s what's is going on 
i hope everything will be  all right '''
print(d)


'''Slicing String
#concatenating two string '''
a="satyam "
b="kumar "
c="jha"
d=a+b+c
print(d)
#help of index we can access the specific string
print(a[2])
print(a[3])
print(a[1])
# help of these method we can access the multiple string in single time(String slicing)
print(a[0:5])

# Shortcut indeces
k="hello dosto "
print(k[0:])
print(k[:6]) # same as 0 to 6
print(k[1:]) # same as 1 to last index

# negative indices
j="Hello gandu "
print(j[-12:-1])# same is k [1:12]
print(j[1:6:3])

# String function

# find length of the string
e="I don't know how to solve the given problem "
print("The length of the e string is : ",len(e))

# if ending are same string then return true else return false
print(e.endswith("problem "))
print(e.endswith("solve "))

# count the specific string how many times appear in the  single string
print("the given sting present in : ",a.count("a"),"times ")
print("the string present in :",e.count("d")," Times ")

# Capitalize - the function change the string into small to capital
y="who are you "
print(y.capitalize())

# (find function ) the string is present or not if string is present he return the index else return the -1 value
print(y.find("are"))
print(y.find("you"))

# Replace ) the function change the oldword into new word in entire string
u="the real og not change the name they change the entity"
print(y.replace("you","Ramesh"))
print(y.replace("who","how"))
print(u.replace("the","so"))