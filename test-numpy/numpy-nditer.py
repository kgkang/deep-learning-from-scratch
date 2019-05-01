import numpy as np


# ra54 = np.random.random((5,4))
ra54 = np.arange(20).reshape(5,4)

print(ra54)

print(ra54[2,3])
print(ra54[(2,3),(3,3)])


it = np.nditer(ra54, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    idx = it.multi_index
    print(idx, '=>', ra54[idx])
    it.iternext()



