'''
    Merge two dictionaries, handling duplicate keys by adding their values.
    d1 = {"a": 10, "b": 20}
    d2 = {"b": 30, "c": 40}
    Result -> {"a":10, "b":50, "c":40}

'''

d1 = {"a": 10, "b": 20,"d":40}
d2 = {"b": 30,"d":50, "c": 40,}
d3={}

for key1,value1 in d1.items():
    d3[key1]=value1

for key,value in d2.items():
    if key in d3:
        d3[key]+=value
    else:
        d3[key]=value

print(d3)