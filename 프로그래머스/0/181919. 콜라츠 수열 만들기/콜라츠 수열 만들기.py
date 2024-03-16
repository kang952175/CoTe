def solution(n):
    answer = [n]
    max_iterations = 1000
    count = 0  
    while n != 1 and count < max_iterations:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        answer.append(n)
        count += 1  
    return answer
