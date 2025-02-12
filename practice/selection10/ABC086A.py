"""
ABC086 A
[問題]
二つの正整数a, b が与えられる.aとbの積が偶数か奇数か判定せよ.
[制約]
・1≦a,b≦10000
・a,bは整数
"""

def solution(x: int, y: int):
    if x % 2 == 0 or y % 2 == 0:
        print("Even")
        return
    
    multi = x * y

    if multi % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    a = int(input("a:"))
    b = int(input("b:"))
    solution(int(a), int(b))