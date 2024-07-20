# 1st game using Python  -->  5th Sept,2022
import random


def comp_choose(comp):
    randNo= random.randint(1, 3)    
    if randNo==1:
        comp= 's'
    elif randNo==2:
        comp= 'w'
    else:
        comp= 'g'  
    return(comp) 


def game_win(c,b):
    if c==b:
        return None
    if c=='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    if c=='w':
        if b=='g':
            return False
        elif b=='s':
            return True
    if c=='g':
        if b=='w':
            return False
        elif b=='s':
            return True
 
        
def result(d):
    if d==None:
        print("Draw match")
    elif d:
        print("You win!")
    else:
        print("You Lose!")

              
a= print("comp turn : snake(s) water(w) or gun(g)?")
b= input("your turn : snake(s) water(w) or gun(g)?")
c=comp_choose(a)
d=game_win(c,b)
print(f"comp choose: {c}")
print(f"you choose: {b}")
print("The Result is: ")
result(d)