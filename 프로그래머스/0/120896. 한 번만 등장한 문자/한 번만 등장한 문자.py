def solution(s):
    answer = ''
    alp_dt = {i : s.count(i) for i in s}
    for i in s:
        if alp_dt[i] == 1:
            answer += i
        elif i not in alp_dt:
            return ''
            
    answer = ''.join(sorted(answer))
    return answer