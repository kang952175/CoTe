def solution(num_list:int):
    answer = 0
    first_min_index = []
    min_value = 0
    for i in num_list:
        if i < min_value:
            min_value = i
            first_min_index.append(num_list.index(min_value))
    if len(first_min_index) >= 1:
        answer = first_min_index[0]
    else:
        answer = -1
    
    
    return answer