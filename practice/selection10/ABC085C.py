"""
アイデア
N枚の時の合計額をすべて計算.
その合計がY円であるときに、枚数を記録しておく.

悩み
・for文3回回せば総当たり行けるが、O(N^3)の時間量となってしまう.
   →1000円の枚数= N - (10000円の枚数 + 5000円の枚数)
"""
def check_otoshidama(N: int, Y: int):
    for i in range(N+1): # 10000円の枚数.
        for j in range(N+1-i): # 5000円の枚数.
            k = N - i -j #1000円札の枚数.  
            if Y == 10000*i + 5000*j + 1000*k and N == i+j+k :
                print(i, j, k)
                return
    print(-1, -1, -1)


N, Y = map(int, input().split())
check_otoshidama(N, Y)



#⇓O(N^3)
# for i in range(N): # 10000円の枚数.
#     for j in range(N): # 5000円の枚数. 
#         for k in range(N): # 1000円の枚数.
#             if Y == 10000*i + 5000*j + 1000*k and N == i+j+k:
#                 print(i, j, k)
#                 break

