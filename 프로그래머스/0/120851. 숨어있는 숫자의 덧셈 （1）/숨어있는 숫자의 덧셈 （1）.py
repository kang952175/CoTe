import re

def solution(my_string):
    answer = 0
    numbers = re.findall('\d', my_string) 
    for num in numbers:
        answer += int(num)
    return answer
