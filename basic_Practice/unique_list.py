'''
    Write a function unique_elements(lst) that returns a list of elements 
    that appear only once in the given list.

'''

def unique_elements(lst):
    new_lst=[]
    for i in lst :
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
l=[]
element=input("Enter the element to append: ")
l.append(element)
while(True):
    
    choice=input("Do you want to fill in the list:(Y/N)").lower()
    if choice == "y":
       element=input("Enter the element to append: ")
       l.append(element)
    else:
        break    
print(l)
l2=unique_elements(l)
print("New List:")
print(l2)