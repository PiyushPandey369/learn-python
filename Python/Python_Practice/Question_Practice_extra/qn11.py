'''
    Write a program to swap the key value pair for max and min values
    Eg if the dict is like this {‘a’:1,’b’:2,’c’:3}
    Output should be {a:3,b:2,c:1}

'''

data = {'a': 1, 'b': 2, 'c': 3,'d':9}


min_val = min(data.values())
max_val = max(data.values())

print(data)

result = {}
for k, v in data.items():
    if v == min_val:
        result[k] = max_val
    elif v == max_val:
        result[k] = min_val
    else:
        result[k] = v

print(result)
