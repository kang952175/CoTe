def solution(slice, n):
    if n % slice:
        answer = n // slice + 1
    else:
        answer = n // slice
    return answer