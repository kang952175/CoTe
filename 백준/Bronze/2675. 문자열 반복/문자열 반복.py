T = int(input())

for _ in range(T):
    R, S = input().split()
    P = ''
    for char in S:
        P += char * int(R)
    print(P)
