# Wildqat をインポート
import wildqat as wq

# 計算をするためのオブジェクトを作成
a = wq.opt()
# QUBO 行列を定義
a.qubo = [[-3,4,-2],[0,-5,6],[0,0,3]]
# 計算実行
a.sa()
