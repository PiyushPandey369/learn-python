'''
    Guess The number

'''

import random as r

comp_num=r.randint(0,100)
count=0
while(True):
    num=int(input("Enter the number to guess:"))
    count=count+1
    if(num==comp_num):
        print("You Guessed Correctly")
        break
    elif(num>comp_num):
        print("Target_Number is smaller")
    else:
        print("Target_Number is larger")

print(f"You guessed in {count} attempts")
    
