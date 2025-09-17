'''
     Count the frequency of a particular character in a provided string.
     Eg 'hello how are you' is the string, the frequency of h in this 
     string is 2.

'''

words=input("Enter the string:")
dict={}

for i in words:
    if i not in dict:
        if i==" ":
            continue
        value=words.count(i)
        key=i
        dict[key]=value

print(dict)
        
    
        