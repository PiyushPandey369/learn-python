'''
    Write a program that counts the frequency of each character in a string 
    and stores it in a dictionary.

'''

words=input("Enter the string:")
dict={}
value=0
key=""
for i in words:
    if i not in dict:
        if i==" ":
            continue
        value=words.count(i)
        key=i
        dict[key]=value
print(dict)