def receipt_cal(n):
    total_price = 0
    for _ in range(n):
        price, count = map(int, input().split(' '))
        total_price += (price * count)
    return total_price

if __name__ == "__main__":
    X = int(input())
    N = int(input())
    total_price = receipt_cal(N)
    if X == total_price:
        print("Yes")
    else: print("No")