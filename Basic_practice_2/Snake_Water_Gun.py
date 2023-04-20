import random
def game(comp,you):
    if comp == you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


randno= random.randint(1,3)
print("Comp Turn: Snake(s) Water(w) Or Gun(g)?")
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

you=input("Your Turn: Snake(s) Water(w) Or Gun(g)?")
a= game(comp,you)

print(f"computer Chose {comp}")
print(f"You Chose {you}")

if a==None:
    print("game is Tie")
elif a:
    print("You Win")
else:
    print("You Lose!")