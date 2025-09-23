'''
    Write a function is_palindrome(word) that checks
    if a string is a palindrome (ignore spaces and case).

'''

def is_palindrome(word):
    new_str=word[::-1]
    if new_str==word:
        print(f"{new_str} is palindrome")
    else:
        print(f"{word} is not palindrome")

word=input("Enter the string: ").replace(" ","").lower()

print(word)
is_palindrome(word)
