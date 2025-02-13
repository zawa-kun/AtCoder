#鏡持ち問題.setとlistどっちが早いんだろう.
import time

N = 10**6  # 100万個のデータ
import random
d = [random.randint(1, 10**6) for _ in range(N)]  # ランダムな値を生成

start = time.time()

d.sort(reverse=True)  # 降順ソート
count = 1
for i in range(1, len(d)):  # 隣り合う要素を比較
    if d[i] < d[i-1]:
        count += 1

end = time.time()
print(f"sort() を使った場合: {end - start:.6f} 秒")


start = time.time()

unique_count = len(set(d))  # set にしてユニークな個数を取得

end = time.time()
print(f"set() を使った場合: {end - start:.6f} 秒")
