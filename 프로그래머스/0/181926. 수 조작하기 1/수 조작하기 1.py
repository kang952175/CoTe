def solution(n: int, control: str):
    keys = {"w": 1,"a": -10,"s": -1,"d": 10}
    
    answer = n
    for i in control:
        answer += keys[i]
    
    return answer