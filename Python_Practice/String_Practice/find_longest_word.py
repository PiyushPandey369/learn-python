'''
    Write a program to find the longest word in a string.

'''
def check_words(w):
    l=[]
    count1=0
    l=w.split()
    for i in l:
        
        if(count1<len(i)):
            str=i
            count1=len(i)
    return str
words=input("Enter the sentence:")
longest_words=check_words(words)
print(longest_words)