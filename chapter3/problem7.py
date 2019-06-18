import wildqat as wq

for i in range(5):
    a = wq.opt()
    a.qubo =  [[-1,4,0,4],
               [0,-1,4,4],
               [0,0,-1,0],
               [0,0,0,-1]]
    print(a.sa())
    print(a.E[-1])  #  a.E[-1] に H の値が格納されています。
