# wap a program to find greater of four no entered by the user.
'''a=input("enter your first number a :")
b=input("enter your second number b: ")
c=input("enter your third number c:")
d=input("enter your fourth number d: ")
if(a>=b and a>=c and a>=d):
    print("a is greater number :")
elif(c >= a and c >= b and c >= d):
        print("c is greater number :")
elif(b >= a and b >= c and b >= d):
            print("b is greater number :")
else:   print("d is greater number :")'''


# Question 2 is wap to find out wheather a student is pass or fail, if it requires total 40% and
# at least 33% in each subject to pass assume 3 subject and take marks as an input from the user.
'''
a=int(input("enter your subject 1 mark :"))
b=int (input("enter your subject 2 mark: "))
c=int (input("enter your subject 3 mark :"))
if(a<33 or b<33 or c<33):
    print(" you are fail :")
if(a+b+c)/3 <40:
    print("you are fail because of less mark")
else:print("you are passed ")
'''

# a spam comment is definded as a text containing following keywords
# make a bt of money" "but now" "subscribe this " "click this" wap to delete these spam
'''
text=input(" Enter the text ")
spam =False
if("make a bt of money"in text):
    spam=True
elif("Buy now"in text):
    spam=True
elif("click this"in text):
    spam=True
else:
    spam=False


 if(spam):
     print("present")
 else:print("not present ") '''
'''
# Q is write a program to find wheather a given username contain less than 10 character or not :
a="satyam kumar jha"
if(len(a)<10):
    print("less than")
else:
    print(len(a))
    print("greater than 10")


  # wap to find out wheather a given name is present in a list or not.
    ks=["satyam","sasfj","dshf"]
    print(ks)
    ke=input("enter your name")
    if(ke in ks):
        print("present")
    else: print("absent")

    # wap to calculate the grade of a student from his marks from the following scheme
    # 90-100 ex  80-90 a 70-80 b 60-70 c 50-60 d <50 fail
    mark=int(input("enter your marks "))
    if mark>=90:
        print("excellent ")
    elif mark>=80:
        print("a grade ")
    elif mark >= 70:
        print("b grade ")
    elif mark >= 60:
        print("c grade ")
    else:print("fail")

    print("your grade is ",mark) '''

name=["satyam","kumar","jha"]
if("satyam"in name):
    print("yes Present ")
else:print("not present ")