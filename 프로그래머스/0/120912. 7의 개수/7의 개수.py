def solution(array):
    answer = 0
    num_dt = {i: str(i).count('7') for i in array }
    for i in array:
        if i in num_dt:
            answer += num_dt[i]            
        else:
            answer = 0
    return answer