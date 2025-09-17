''' 
    Write a program that can sort a given unsorted list. Dont use any built in
    function for sorting.

'''

l=[2,6,1,0,-1,89]

print(l)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
            
print(l)