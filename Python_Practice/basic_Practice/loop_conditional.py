
'''
    Write a Python program that prints all numbers from 1 to 100 but:

    Print "Fizz" for multiples of 3,

    "Buzz" for multiples of 5,

    "FizzBuzz" for multiples of both.

'''

for i in range(0,101):
    if((i%5 == 0) and (i%3==0)):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    
    
    