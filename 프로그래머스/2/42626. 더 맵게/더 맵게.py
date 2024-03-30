import heapq

def solution(scoville, K):
    num = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville) 
        b = heapq.heappop(scoville)  
        new = a + (b * 2)  
        heapq.heappush(scoville, new)  
        num += 1
        
    if scoville[0] < K:
        return -1 
    
    return num
