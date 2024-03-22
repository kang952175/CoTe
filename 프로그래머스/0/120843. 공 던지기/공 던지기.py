def solution(numbers, k):
    answer = 0
    tmp = []
    index = 0
    for _ in range(k):
        tmp.append(numbers[index])
        index = (index + 2) % len(numbers)
    
    answer = tmp[k-1]
    return answer
