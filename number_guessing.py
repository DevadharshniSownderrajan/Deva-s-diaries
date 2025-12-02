import random
Guess=random.randint(1,10)
attempts=0
while Guess>0:
     num=int(input("Enter your number:"))
     if num==Guess:
         print("You got it")
         attempts+=1
         break
     elif num>Guess:
         print("Too high!,try again")
         attempts+=1
     elif num<Guess:
            print("Too low!,try again")
            attempts+=1
print("No.of attempts:",attempts)
    
