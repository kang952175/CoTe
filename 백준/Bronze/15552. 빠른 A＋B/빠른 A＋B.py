import sys

def plus(a, b):
    return a + b

if __name__ == "__main__":
    
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().rsplit())
        result = plus(a, b)
        print(result)
    
