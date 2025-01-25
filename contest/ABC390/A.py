"""12345"""
A = list(map(int,input().split()))

ans = 0

"""
リストインデックスについて
最初range(0,3)とし、意図した動きをしなかった。

⇒range(4)では 0, 1. 2, 3
を生成する。
"""
for i in range(4):
    B = A.copy()
    if A[i] >= A[i +1]:
        A[i] = B[i+1]
        A[i+1] = B[i]
        ans+=1
    # print(A,ans)
    

if ans == 1:
    print("Yes")
else:
    print("No")        
    