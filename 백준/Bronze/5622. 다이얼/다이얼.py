word = input().strip()

dial = {char: (ord(char) - ord('A')) // 3 + 3 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
dial['S'], dial['V'], dial['Y'], dial['Z'] = 8, 9, 10, 10

time = 0

for char in word:
    time += dial[char]

print(time)