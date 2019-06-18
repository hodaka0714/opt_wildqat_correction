import wildqat as wq
import numpy as np

H_A = np.array([
    [-15, 6, 8, 6, 8],
    [0, -6, 6, 4, 6],
    [0, 0, -13, 6, 10],
    [0, 0, 0, -10, 6],
    [0, 0, 0, 0, 23]])
H_B = np.array([
    [-3, 0, 0, 0, 0],
    [0, -2, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 0, -5]])
k, l = 1, 2

a = wq.opt()
a.qubo = k * H_A + l * H_B

for i in range(5):
    print("x = {}".format(a.sa()))
    print("H = {}".format(a.E[-1]))
