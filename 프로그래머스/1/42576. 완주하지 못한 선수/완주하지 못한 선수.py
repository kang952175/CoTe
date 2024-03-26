from collections import Counter
def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    answer = list(result.keys())[0]
    return answer
