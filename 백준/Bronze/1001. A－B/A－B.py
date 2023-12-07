def sub(a,b):
    return a - b

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    answer = sub(a, b)
    
    print(answer)