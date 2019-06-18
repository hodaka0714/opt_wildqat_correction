import wildqat as wq

for i in range(5):
    a = wq.opt()
    a.qubo =  [[-2,2,2,0,0],
               [0,-3,2,2,0],
               [0,0,-3,0,2],
               [0,0,0,-2,2],
               [0,0,0,0,-2]]
    print(a.sa())
    print(a.E[-1])
