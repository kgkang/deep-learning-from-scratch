
import numpy as np

def gradient(f,x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x):
        tmp_val = x[idx]
