'''
     try-except-finally
'''
try:
    a = int(input("Enter number: "))
    b = int(input("Enter second number: "))
    print("Division:", a / b)
except Exception as e:
    print("Error:", e)
finally:
    print("This is from finally")
  


