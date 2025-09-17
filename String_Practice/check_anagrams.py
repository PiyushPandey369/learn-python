'''
    Write a program to check if two strings are anagrams of each other.

'''

def check_anagrams(w1,w2):

    l1 = sorted(w1.lower())
    l2 = sorted(w2.lower())

    if l1==l2:
        print(f"{w1} and {w2} are anagrams")
    else:
        print(f"{w1} and {w2} are not anagrams")
        
word1=input("Enter any words:").lower()
word2=input("Enter another word:").lower()
check_anagrams(word1,word2)