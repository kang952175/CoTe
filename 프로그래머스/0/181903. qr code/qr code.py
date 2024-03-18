def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        remainder = i % q
        if remainder == r:
            answer += code[i]    
    return answer