def solution(emergency):
    answer = []
    importance = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(importance.index(i)+1)
    return answer