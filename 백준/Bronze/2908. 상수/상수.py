a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
    answer = a
else:
    answer = b

print(answer)
