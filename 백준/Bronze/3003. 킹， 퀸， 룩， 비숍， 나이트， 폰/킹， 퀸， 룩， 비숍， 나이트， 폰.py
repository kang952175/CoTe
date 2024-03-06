N = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]

missing_pieces = [str(chess[i] - N[i]) for i in range(len(chess))]

print(" ".join(missing_pieces))
