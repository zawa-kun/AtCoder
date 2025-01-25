N = int(input())
A = list(map(int,input().split()))
flag = True

for i in range(len(A)-2):
    if A[i+1]**2 != A[i]*A[i+2]:
        flag= False

if flag:
    print("Yes")
else:
    print("No")