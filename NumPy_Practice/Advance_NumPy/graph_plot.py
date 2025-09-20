import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,50)
y=x

# plt.plot(x,y) -> straight line
# plt.plot(x*x,y) -> parabola
# plt.plot(x,np.sin(x)) -> sine function
denominator = 1 + np.exp(-x)
z=1 / denominator
plt.plot(x,z) # -> sigmoid function

plt.show()
