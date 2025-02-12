"""
ABC083B
"""
# 関数：各桁の和を計算する
def digit_sum(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10 #各桁を取り出す.
        n //= 10
    return sum


N, A, B = map(int, input().split())
result = 0

for i in range(N+1):
    sum = digit_sum(i)
    #もし,A以上B以下であればiをresultに加算.
    if sum >= A and sum <= B:
        result += i

print(result)

        
        