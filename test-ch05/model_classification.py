
import numpy as np
import matplotlib.pylab as plt

def sigmod(z):
    return 1 / (1 + np.exp(-z))


sz = np.linspace(-10,10,100)
sa = sigmod(sz)

plt.plot(sz, sa)
plt.show()

