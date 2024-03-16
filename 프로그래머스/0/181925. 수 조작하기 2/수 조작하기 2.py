def solution(numLog):
    answer = ''
    control = {1: 'w', -1:'s', 10:'d', -10:'a'}
    for i in range(1,len(numLog)):
        action = numLog[i] - numLog[i-1]
        answer += control[action]
    
    return answer