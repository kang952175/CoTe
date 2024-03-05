import string

S = input()

for a in string.ascii_lowercase:
    if a in S:
        print(S.index(a), end=' ')
    else:
        print(-1, end=' ')
