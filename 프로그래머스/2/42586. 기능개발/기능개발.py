from collections import deque

def solution(progresses, speeds):
    answer = []
    p_qu = deque(progresses) 
    s_qu = deque(speeds)  

    while p_qu:  
        complete = 0  
        
        for i in range(len(p_qu)):
            p_qu[i] += s_qu[i]
        

        while p_qu and p_qu[0] >= 100:
            p_qu.popleft()  
            s_qu.popleft()
            complete += 1 
        
        if complete > 0:
            answer.append(complete)  
    return answer
