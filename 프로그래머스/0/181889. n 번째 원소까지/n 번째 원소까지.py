from typing import List

def solution(num_list:List[int], n:int):
    answer = []
    answer.extend(num_list[:n])
    
    return answer