# coding: utf-8

import numpy as np


x = [3]*4
print(x)
# [3, 3, 3, 3]

y = [5]*4
z = x+y
print(z)
# [3, 3, 3, 3, 5, 5, 5, 5]

ax = np.array([3]*4, dtype='int32')
print(ax)
# [3 3 3 3]

ay = np.array(y)
az = ax + ay
print(az)

azz = np.add(ax,ay)
print(azz)