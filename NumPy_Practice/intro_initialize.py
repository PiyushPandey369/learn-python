import numpy as np

# np.ones, np.zeros, np.random are used to initialize the array

# np.ones -> generate 1 of given dimensions (By default float)
a=np.ones((3,3,3))
print(a)

# np.zeros -> generate 0 of given dimensions
b=np.zeros((3,3,3))
print(b)

# np.random() -> generates random value between 0 and
c=np.random.random((3,4))
print(c)

# np.linspace() -> -10 is lower bound, 10 is upper bound, 10 is number of items to generate
# np.linspace() -> generates equal distance elements
d=np.linspace(-10,10,10)
print(d)

# np.identity -> generates given order identity matrix 
# np.eye() -> provides more control
e=np.identity(4)
print(e)