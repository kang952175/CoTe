def solution(num_list):
    answer = num_list
    if num_list[-1] > num_list[-2]:
        val = num_list[-1] - num_list[-2]
        answer.append(val)
    else:
        val = num_list[-1] * 2
        answer.append(val)
        
    return answer