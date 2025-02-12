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