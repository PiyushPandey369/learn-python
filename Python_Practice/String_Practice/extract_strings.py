
'''
    Give a string (e.g: "PythonProgramming",) extract:

    All uppercase letters

    All lowercase letters

    Characters at even index positions

'''
word="PythonProgramming"
print("Uppercase: ")
for i in word:
    if i.isupper():
        print(i,end=" ")
print("\nLowercase: ")
for i in word:
    if i.islower():
        print(i,end=" ")
new_words=word[::2]
print("\nCharacters at even index positions")
print(new_words)

