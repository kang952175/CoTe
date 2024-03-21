def solution(array, n):
    answer = 0
    min_diff = float('inf')
    for v in array:
        diff = abs(n - v)        
        if diff < min_diff or (diff == min_diff and v < answer):
            min_diff = diff
            answer = v
    return answer
