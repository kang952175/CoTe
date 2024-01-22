def plus(a, b):
    return a + b

if __name__ == "__main__":
    while True:
        try:
            a, b = map(int, input().split())
            result = plus(a, b)
            print(result)
        except:
            break