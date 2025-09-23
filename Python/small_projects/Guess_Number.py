'''
num=75
user=6
if(num==user)
you guessed it.
elif(num>user)
Guess more than that
else
Guess less than 

'''
import random

def select_random():
    return random.randint(0, 100)
num=select_random()
count_attempt=1
import time 
time.sleep(1)
print("Welcome To The World Of Guessing Number")
time.sleep(5)
guess=int(input("Guess the number from(0-100):"))
while (guess>0 and guess<101):
    if(guess>num):
        print("Guess The Number Less Than That")
    elif(guess<num):
        print("Guess The Number Greater Than That")
    else:
        print("Congraulation! You Guess Is Correct.")
        print(f"You Guessed Number {num} in {count_attempt} attempts.")
        break
    guess=int(input("Guess the number from(0-100):"))
    count_attempt+=1
print("Game Over!")

        
    



