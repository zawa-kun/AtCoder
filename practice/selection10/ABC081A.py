"""
ABC 081
[問題]
0と1とのみから成る3桁の番号sが与えられる。1が何個含まれているか求める.
"""

s = str(input())

count = 0

if s[0] == "1":
    count += 1

if s[1] == "1":
    count += 1

if s[2] == "1":
    count += 1

print(count)  