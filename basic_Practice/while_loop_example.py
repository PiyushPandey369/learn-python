'''
    Using a while loop, take input from the user until they type "stop".
    Count how many valid integers they entered.
    
'''

count = 0

while True:
    user = input("Enter an integer: ")
    
    if user.lower() == "stop":
        print("Total valid integers entered:", count)
        break
    
    if user.isdigit():   # checks if all characters are digits
        count += 1
    else:
        print("Not a valid integer, try again!")
