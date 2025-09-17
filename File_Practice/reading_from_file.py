'''
    Write a program that reads numbers.txt and prints only the even numbers.

'''

with open("numbers.txt") as f:
    even1=f.readlines()
    for i in even1:
        if (int(i)%2==0):
            print(i)
    


