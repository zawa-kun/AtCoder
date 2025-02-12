"""
ABC087B
"""
A, B, C = map(int,input().split())
X = int(input())
# totals = [] #totalsを無くす事でメモリ使用量を削減.
count = 0

#各硬貨の枚数の範囲で組み合わせを試す.
for i in range(A+1): #500
    for j in range(B+1): #100
        for k in range(C+1): #50
            #合計額の計算.
            total = 500*i + 100*j + 50*k
            #目標金額と一致したらカウントを増やす.
            if total == X:
                count += 1

# for i in range(len(totals)):
#     if totals[i] == X:
#         count += 1

print(count)
    