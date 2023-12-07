def mul(a, b):
    return a * b

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    answer = mul(a, b)
    
    print(answer)
    