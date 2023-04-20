'''def palindrom(num):
    rev=num[::-1]
    if(num==rev):
        print("palindrome number ")
    else:print("not a palindrome no")



#a=input("enter anything")
#palindrom(a)


def prime(num):
    if(num==1):
        print("it is not a prime number")
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                print("it is not a prime number")
                break
        else:
         print("it is a prime number")

a=int(input("enter a number"))
prime(a)



def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)

fact(5)



def arm(num):
    number=num
    sum=0
    while num>0:
        rem=num%10
        cube=rem*rem*rem
        sum=sum+cube
        num=num//10
    if(sum==number):
        print("it is a armstrong number")
    else:
        print("it is not a armstrong number")


arm(153)




def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("not a prime")
            break
        else:print("prime")
        break

prime(7)




#def arms(num):
 #number=num
 #while num>0:




#arms(9474)





sorting=["kolkata","Delhi","Bihar","Kashmir","Uttart_Pradesh"]
sorting.sort()
print(sorting)
upr=(a.upper() for a in sorting)
print(upr)


Dict1={
    "brand":"Maruti",
    "model":"wagno",
    "Year": "2018",
    "year": "2022"
}
print(Dict1.keys())
print(Dict1.values())






rt=["Kolkata","delhi","Mumbai"]
rt.insert(4,"Kathmandu")
print(rt)
'''

sorting=["kolkata","Delhi","Bihar","Kashmir","Uttart_Pradesh"]
del sorting[2]
print(sorting)