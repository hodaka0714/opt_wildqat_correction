import wildqat as wq 　　# wildqat をインポート

a = wq.opt() 　　　　　　 # 計算をするためのオブジェクトを作成
a.qubo = [[3,0],[0,-2]] # QUBO 行列を定義
a.sa() 　　　　　　　　    # 計算実行
