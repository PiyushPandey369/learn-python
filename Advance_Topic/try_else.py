'''
    try-except and else block
'''
try:
    a=int(input("Enter number:"))
    b=int(input("Enter second number:"))
except Exception as e:
    print(e)    
else:
    print(a+b)
