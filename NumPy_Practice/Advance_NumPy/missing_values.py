# missing value

import numpy as np

# np.nan -> missing values

a=np.array([1,2,3,4,np.nan,6,np.nan])
print(np.isnan(a)) # -> returns nan value
print(a[np.isnan(a)]) # -> returns True for nan value
print(a[~np.isnan(a)])




