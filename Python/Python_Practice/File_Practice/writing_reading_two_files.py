'''
    Write a program to copy the contents of one file (source.txt) 
    into another (destination.txt).

'''

sms=input("Enter the message to write:")

with open("source.txt","w") as f:
    f.write(sms)
    
with open("source.txt",) as f1:
    sms1=f1.readlines()

with open("destination.txt","w") as f2:
    f2.write(str(sms1))