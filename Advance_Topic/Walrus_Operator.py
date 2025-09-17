''' 
    Walrus Operator
'''
if (n := len(data := input("Enter some string:"))) > 5:
    print(f"{data} has length {n} characters")
