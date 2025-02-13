N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True) #降順にソート.

Alice = 0 #アリスの点数.
Bob = 0 #ボブの点数.

flag = True #カードを取る人をフラグで管理.

#カードをN回ドロー.
for _ in range(N):
    if flag:
        Alice += a[0]
        a.pop(0) #加算したものから順番に取り除いていく.
        flag = False
    else:
        Bob += a[0]
        a.pop(0)
        flag = True
    
print(Alice - Bob) #AliceとBobの差.



"""
コードレビュー
1 pop(0)は非効率
・pop(0)を使うと非効率.リストの先頭要素を削除する為、その度二シフトをする必要があり、O(N)の計算量がかかる.

2 フラグを使わず、enumrateを使うト簡潔になる.
ループの偶奇でAlice/Bobを判断した方がシンプルになる.
例⇓⇓⇓
# 偶数番目 (Alice) / 奇数番目 (Bob) で分ける
for i, card in enumerate(a):
    if i % 2 == 0:
        Alice += card
    else:
        Bob += card
"""
