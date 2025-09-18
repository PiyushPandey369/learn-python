'''
    Check if one set is a subset of another without using issubset().

'''

s1={1,2,3}
s2={1,2}
is_subset = True
for elem in s2:
    if elem not in s1:
        is_subset = False
        break

print(is_subset)
print(s2.issubset(s1)) 
