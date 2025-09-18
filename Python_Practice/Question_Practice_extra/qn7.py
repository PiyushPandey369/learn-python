'''
    Write a program that can convert a 2D list
    to 1D  list. Write a program that can print
'''

l1=[[1,0],[2,4],[4,9],[1,2]]

l2=[]
print(l1)
for i in l1:
    for j in i:
        l2.append(j)
        
print(l2)