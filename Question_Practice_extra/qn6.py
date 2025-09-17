'''
    Write a python program to search a given number from a list
'''

l=[2*i for i in range(1,11)]

elem=int(input("Enter the element to search"))

print(l)
def search_fxn(n):
    if n==elem:
        return True
    else:
        return False
    
res=(filter(search_fxn,l))
print(list(res))