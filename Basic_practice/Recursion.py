# Q  find factorial of n no using recursion
def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n*facto(n-1)


print(facto(5))

def fun(d):
    ded=1
    for i in range(d):
        ded=ded*i+1
        return ded


    print(fun(5))
