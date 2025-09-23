'''
    Write a program that checks whether a number is a 
    prime number or not (using for loop and else clause).
    
'''

num=int(input("Enter the number:"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")