from collections import deque

def solution(priorities, location):
    """
    1. (중요도, 위치) 튜플을 원소로 하는 큐를 생성합니다. 여기서 위치는 문서의 초기 위치를 의미합니다.
    2. 큐가 비어있지 않은 동안, 큐에서 프로세스를 하나씩 꺼냅니다.
    3. 꺼낸 문서보다 중요도가 높은 문서가 큐 안에 존재한다면, 꺼낸 프로세스를 큐의 끝에 다시 추가합니다.
    4. 그렇지 않다면 (즉, 꺼낸 프로세스가 현재 가장 중요도가 높다면), 해당 프로세스를 인쇄합니다. 이때 위치 카운트를 하나 증가시킵니다.
    5. 찾고자 하는 프로세스가 실행되면, 그 시점의 위치 카운트를 반환합니다.
    """
    # initialize : (중요도, 원래 위치) 
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    while queue:
        current = queue.popleft()
        if any(current[0] < other[0] for other in queue):
            queue.append(current) 
        else:
            answer += 1  
            if current[1] == location:
                break

    return answer