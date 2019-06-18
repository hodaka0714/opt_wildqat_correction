import wildqat as wq
import numpy as np

H_A = np.array([
    [2, -2, -2, 0, 0, 0],
    [0, 3, -2, -2, 0, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 3, -2, -2],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0,1 ]])
H_B = np.array([
    [-5, 2, 2, 2, 2, 2],
    [0, -5, 2, 2, 2, 2],
    [0, 0, -5, 2, 2, 2],
    [0, 0, 0, -5, 2, 2],
    [0, 0, 0, 0, -5, 2],
    [0, 0, 0, 0, 0, -5]])
k, l = 1, 3

a = wq.opt()
a.qubo = k * H_A + l * H_B

for i in range(5):
    print("x = {}".format(a.sa()))
    print("H = {}".format(a.E[-1]))
