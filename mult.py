import sys
import numpy as np

np.random.seed (0)

n = int (float (sys.argv[1]))
A = np.random.normal (size = (n, n))
B = np.random.normal (size = (n, n))
C = np.matmul (A, B)
