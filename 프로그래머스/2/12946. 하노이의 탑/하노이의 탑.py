def solution(n):
    answer = []  
    def hanoi(n, st, to, end):       
        if n == 1:
            answer.append([st, end])  
        else:
            hanoi(n-1, st, end, to)  
            answer.append([st, end]) 
            hanoi(n-1, to, st, end)  

    hanoi(n, 1, 2, 3) 
    return answer  