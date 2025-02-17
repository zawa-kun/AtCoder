#!/bin/python3

# import math
# import os
import random
# import re
# import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar) -> int:
    # Write your code here
    count = 0
    while ar:
        flag = True #ペアが見つかったか管理するフラグ.
        for i in range(1,len(ar)):
            if ar[0] == ar[i]: # 同じ数値探し
                flag = False
                count += 1
                ar.pop(i) #先に0番目からpopすると,popするべき値がずれてしまう(i-1になってしまう)ので先にi
                ar.pop(0) #ペアが見つかった組は取り除く.
                break
    
        if flag:
            ar.pop(0)
        
    return count   
    


# n = int(input().strip())
n = 9
# ar = list(map(int, input().rstrip().split()))
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(n, ar)

print(result)