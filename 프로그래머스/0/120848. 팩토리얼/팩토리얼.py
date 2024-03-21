def solution(n):
    i = 1
    factorial = 1
    while True:
        if factorial > n:
            break
        i += 1
        factorial *= i
    return i - 1