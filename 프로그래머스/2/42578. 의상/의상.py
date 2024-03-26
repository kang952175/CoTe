def solution(clothes):
    hash_maps = {}  

    for _, category in clothes:
        if category in hash_maps:
            hash_maps[category] += 1
        else:
            hash_maps[category] = 1

    answer = 1  
    for key in hash_maps:
        answer *= (hash_maps[key] + 1) # 안 입는 경우 +1

    return answer - 1 # 전체 안 입는 경우의 수 하나 제외