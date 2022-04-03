import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
t = np.arange(-2, 3.01, 5)
sp = plt.subplot(111)
sp.plot(x, x * x - x - 6,  t, t*0, 'ro')
sp = plt.subplot(111)
sp.plot(x,0*x)
plt.axis('equal')

plt.show()