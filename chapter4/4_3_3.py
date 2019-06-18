import wildqat as wq
import numpy as np

H_A = np.array([
    [-5, 2, 2, 2, 2, 2],
    [0, -5, 2, 2, 2, 2],
    [0, 0, -5, 2, 2, 2],
    [0, 0, 0, -5, 2, 2],
    [0, 0, 0, 0, -5, 2],
    [0, 0, 0, 0, 0, -5]])
H_B = np.array([
    [0, -1, -1, 0, 0, -1],
    [0, 0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, -1],
    [0, 0, 0, 0, 0, 0]])
k, l = 2, 1

a = wq.opt()
a.qubo = k * H_A + l * H_B

for i in range(5):
    print("x = {}".format(a.sa()))
    print("H = {}".format(a.E[-1]))
