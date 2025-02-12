"""
ABC081B
"""

N = int(input())
A = list(map(int, input().split()))
count = -1
flag = True

#操作がおこなえる限り操作を繰り返す.
#flagで操作回数を制御.
while flag:
    for i in range(N):
        #奇数が存在したら,即操作終了.
        if A[i] % 2 != 0:
            flag = False
            break

        A[i] = A[i]//2

    count += 1 #操作回数のカウント.
    

print(count)