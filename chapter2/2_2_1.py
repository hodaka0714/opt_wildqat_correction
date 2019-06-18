import wildqat as wq 　　# Wildqat をインポート

a = wq.opt() 　　　　　　 # 計算をするためのオブジェクトを作成
a.qubo = [[-3,4,-2],[0,-5,6],[0,0,3]] 　 # QUBO 行列を定義
a.sa() 　　　　　　　　    # 計算実行
