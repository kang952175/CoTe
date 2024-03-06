# 체스 피스의 기대 개수
expected = [1, 1, 2, 2, 2, 8]

# 사용자로부터 각 피스의 개수를 입력받음
found = list(map(int, input().split()))

# 각 피스의 기대 개수와 실제 개수의 차이를 계산하고 출력
diff = [e - f for e, f in zip(expected, found)]
print(*diff)

