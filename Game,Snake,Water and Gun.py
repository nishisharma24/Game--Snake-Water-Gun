import random
def gameWin(comp,you):
    if comp==you:
        return None
#if computer chooses snake
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
#if computer chooses water       
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
#if computer chooses gun       
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w': 
            return True
print("comp Turn: Snake(s),Water(w), or Gun(g)?")
randNo=random.randint(1,3) #random function
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=input("your turn: snake(s),water(w) or Gun(g)?")
a=gameWin(comp,you)
print(f"Computer Chose {comp} ")#f string:to show the what computer and you choose.
print(f"You Chose {you} ")
if a==None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Loose!")
input()    

