def add(A,B):
    print(A + B)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split(' '))
        add(A, B)
        