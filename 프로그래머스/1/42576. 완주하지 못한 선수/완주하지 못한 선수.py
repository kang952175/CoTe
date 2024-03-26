def solution(participant, completion):
    hash_map = {}  
    for person in participant:
        if person in hash_map:
            hash_map[person] += 1  
        else:
            hash_map[person] = 1  
    for person in completion:
        hash_map[person] -= 1  
    for person in hash_map:
        if hash_map[person] > 0:
            return person 

    return None  