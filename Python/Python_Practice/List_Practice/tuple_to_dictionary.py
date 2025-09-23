'''
    Convert a tuple of tuples:

    t = (("a", 1), ("b", 2), ("c", 3))

    into a dictionary.
    
'''

t = (("a", 1), ("b", 2), ("c", 3))

d={}

for key,values in t:
    d[key]=values
print(d)
print(type(d))