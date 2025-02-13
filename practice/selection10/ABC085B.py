N = int(input())
d = [int(input()) for _ in range(N)]
d = {int(input()) for _ in range(N)}

d.sort(reverse=True) #降順ソート.

count = 1 #最初の要素は必ずカウント.
for i in range(1,len(d)): # インデックス1から開始.
    if d[i] < d[i-1]:
        count += 1

print(count)

"""
コードレビュー
・受取時,setを使おう!!!
setは
 重複を自動で排除(setの中には同じ要素は2回入れることが出来ない)
 要素の順番がない
 検索・追加・削除が高速(O(1))
 ※リストとの違い
  ・list 順番保持＆重複オッケー
  ・set 順番無し＆重複ＮＧ
"""

"""
N = int(input())
d = {int(input()) for _ in range(N)}  # 集合(set)を使って重複を自動で排除
print(len(d))  # ユニークな要素数を出力

"""