def plus(a, b):
    return a + b

if __name__ == "__main__":
    while True:
        a, b = map(int, input().split())
        if (a == 0 and b == 0):
            break         
        else:
            result = plus(a, b)
            print(result)