import numpy as np

# Stacking is used to join 
# Condition : shape must be same
a1 = np.arange(12).reshape(3, 4)  
a2 = np.arange(12,24).reshape(3, 4)   

print(a1,a2)      
print(np.hstack((a1,a2))) # Horizontal stacking
print(np.vstack((a1,a2))) # Vertical stacking

# Splitting is opposite of Stacking

print(np.hsplit(a1,4)) # Horizontal splitting
print(np.vsplit(a1,3)) # Vertical splitting