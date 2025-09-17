'''
    Write a function count_vowels(s) that returns
    the number of vowels in a string.

'''
def count_vowels(s):
    count=0
    count1=0
    for i in s:
        if(i in "aeiouAEIOU"):
          count=count+1
        else:
            count1+=1
    return count,count1

s=input("Enter any string: ")
length,length1=count_vowels(s)
print(f"The number of vowels is {length}") 
print(f"The number of consonant is {length1}") 