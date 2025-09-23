''' 
     Find number of words in string.

'''

def check_sentences(sen):
    count=0
    in_word=False
    for i in sen:
        if i!=" " and not in_word:
            count+=1
            in_word=True
        elif i==" ":
            in_word=False
    return count
    
words=input("Enter the sentence:")
length=check_sentences(words)
print(f"The number of words in string: {length}")


'''

def check_sentences(sen):
    count=0
    l=[]
    l=sen.split()
    return len(l)
words=input("Enter the sentence:")
length=check_sentences(words)
print(length)
'''