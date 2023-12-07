def add(a, b):
    return a + b

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    answer = add(a, b)
    print(answer)
    
    