# Array Functions
import numpy as np

a1=np.random.random((3,3))
print(a1)

# max/min/sum/prod

# Applying on all elements
print("max/min/sum/prod overall")
print(np.sum(a1))
print(np.max(a1))
print(np.min(a1))
print(np.prod(a1))

# Applying on rows and columns
# columns=0 and rows=1

print("max/min/sum/prod rows and columns wise")
print(np.sum(a1,axis=1)) #sum in each rows
print(np.max(a1,axis=1)) #maximum in each rows
print(np.min(a1,axis=0)) # smallest in each column
print(np.prod(a1,axis=0)) # product of each column 

# mean/median/std/var

print("mean/median/std/var overall")
print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

# trigonometric functions 

print("Trigonometric Values:")
print(np.sin(a1))

# dot product
print("Dot Products:")
b1=np.arange(1,13).reshape(3,4)
b2=np.arange(12,24).reshape(4,3)
print(np.dot(b1,b2))

# log and exp
print("Log and exponential values:")
print(np.log(b1))
print(np.exp(b1))
print(np.exp(np.log(b2)))

# round/floor/ceil
print("Round/Floor/Ceiling values:")
c1=np.random.random((2,2))
print(np.round(c1))
print(np.floor(c1))
print(np.ceil(c1))