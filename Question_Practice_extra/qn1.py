'''
    Extract username from a given email.
    Eg if the email is nitish24singh@gmail.com then the username
    should be nitish24singh
    
'''


email=input("Enter the email id:")

s=email.strip("@gmail.com")

print(s)