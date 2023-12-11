def dice_prize(p, q, r):
    if p == q == r:
        print(10000 + p * 1000)
    elif p == q or p == r:
        print(1000 + p * 100)
    elif q == r:
        print(1000 + q * 100)
    else:
        print( max(p, q, r) * 100 )
    
if __name__ == "__main__":
    a, b, c = map(int, input().split())
    
    dice_prize(a, b, c)