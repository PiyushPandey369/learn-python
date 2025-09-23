'''
    Reverse_String
'''
words=input("Enter the string to reverse:")

l=words.split()
l.reverse()

s=" ".join(l)

print(s)