import random

print("What is your name?")
name=input()

print("well,.."+name+"  I'm thinking of a number 1 and 20")
sn=random.randint(1,20)


for gt in range(1,7):
    print("Take a guess")
    guess=int(input())

    if guess<sn:
        print("Your guess is too low")
    elif guess>sn:
        print("Your guess is too high")
    else:
        break

if sn==guess:
    
    print("Whoaaaa.....That was the number I was thinking of")
    print("You took "+str(sn)+"guesses")
else:
    print("Nope the number I was thinking was"+str(sn))
