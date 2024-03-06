word = input().upper()

counts = [word.count(chr(i)) for i in range(65, 91)]

max_count = max(counts)

if counts.count(max_count) > 1:
    print('?')
else:
    print(chr(counts.index(max_count) + 65))
