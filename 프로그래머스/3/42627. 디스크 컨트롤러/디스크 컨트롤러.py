import heapq

def solution(jobs):
    jobs.sort()
    total_len = len(jobs)
    total_wait = 0
    current_time = 0
    wait_heap = []

    while jobs or wait_heap:
        while jobs and jobs[0][0] <= current_time:
            start, duration = jobs.pop(0)
            heapq.heappush(wait_heap, (duration, start))
        
        if wait_heap:
            duration, start = heapq.heappop(wait_heap)
            current_time += duration
            total_wait += current_time - start
        else:
            current_time = jobs[0][0]
    
    average_wait = total_wait // total_len  
    return average_wait
