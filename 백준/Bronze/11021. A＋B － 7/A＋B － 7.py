def plus_with_text(a, b, i):
    return print(f"Case #{i}: {a+b}")

if __name__ == "__main__":
    T =  int(input())
    for i in range(1, T+1):
        a, b = map(int, input().split())
        plus_with_text(a, b, i)
