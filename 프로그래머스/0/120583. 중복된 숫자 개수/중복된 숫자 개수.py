def solution(array, n):
    answer = {}
    for num in array:
        answer[num] = answer.get(num, 0) + 1

    return answer.get(n, 0)