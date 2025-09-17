'''

    Given a list:

    data = [1, 2, 3, 4, 5, 6]

    Write a program to:

    Square each element using list comprehension

    Extract only even numbers

    Reverse the list without using reverse()
    
'''
def square_list(data):
    d=[]
    for num in data:
        d.append(num**2)
    print(d)

def even_extract(data):
    d=[]
    for num in data:
        if(num%2==0):
            d.append(num)
    print(d)
    
def reverse_list(data):
    d=[]
    for num in reversed(data):
        d.append(num)
    print(d)
    
data = [1, 2, 3, 4, 5, 6]
print("Square Elements")
square_list(data)
print("Even elements")
even_extract(data)
print("Reverse")
reverse_list(data)