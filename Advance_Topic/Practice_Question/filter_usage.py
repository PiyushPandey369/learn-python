'''
    Write a program to filter a list of numbers which are divisible by 5
'''

l=[5,6,70,90,1,10,25,4]
print(l)

def check_div(n):
    if n%5==0:
        return True
    return False

res=filter(check_div,l)
print(list(res))