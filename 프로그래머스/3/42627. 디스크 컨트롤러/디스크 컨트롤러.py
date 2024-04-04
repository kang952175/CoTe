import heapq

def solution(jobs):
    # 작업이 요청되는 시점으로 정렬
    jobs.sort()
    total_len = len(jobs)
    total_wait = 0
    current_time = 0
    wait_heap = [] # 현재 시간에 처리할 수 있는 작업들을 관리할 힙

    while jobs or wait_heap:
        # 현재 시간 이하로 요청된 모든 작업을 힙에 추가
        while jobs and jobs[0][0] <= current_time:
            start, duration = jobs.pop(0)
            heapq.heappush(wait_heap, (duration, start))
        
        if wait_heap:
            # 힙에서 처리 시간이 가장 짧은 작업을 선택
            duration, start = heapq.heappop(wait_heap)
            current_time += duration
            total_wait += current_time - start
        else:
            # 대기 중인 작업이 없다면, 다음 작업의 시작 시간으로 시간을 조정
            current_time = jobs[0][0]
    
    # 평균 대기 시간 계산
    average_wait = total_wait // total_len  # 소수점 이하를 버림
    return average_wait
