'''
    Count the number of vowels in a string provided by the user.

'''

words=input("Enter the string:")
count=0
dict={}
for i in words:
    if i in "AEIOUaeiou":
        count=count+1
        if i not in dict:
            value=words.count(i)
            key=i
            dict[key]=value
        
print(dict)    
print(count)