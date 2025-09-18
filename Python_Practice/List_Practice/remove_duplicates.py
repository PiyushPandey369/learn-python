'''
    Write a program to remove duplicates from a list while maintaining order.
    
'''

l=[1,1,2,3,4,2,3,4]

new_lst=[]
for i in l :
        if i not in new_lst:
            new_lst.append(i)
print(new_lst)