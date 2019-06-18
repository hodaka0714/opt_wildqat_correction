import wildqat as wq
import numpy as np

H_A = np.array([
    [-1, 0, 0, 0, 0, 0, 2, 0],
    [0, -1, 0, 0, 0, 0, 2, 2],
    [0, 0, -1, 0, 0, 0, 2, 2],
    [0, 0, 0, -1, 0, 0, 2, 0],
    [0, 0, 0, 0, -1, 0, 0, 2],
    [0, 0, 0, 0, 0, -1, 0, 2],
    [0, 0, 0, 0, 0, 0, -4, 4],
    [0, 0, 0, 0, 0, 0, 0, -4]])
H_B = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])
k, l = 5, 1

a = wq.opt()
a.qubo = k * H_A + l * H_B

for i in range(5):
    print("x = {}".format(a.sa()))
    print("H = {}".format(a.E[-1]))
