import heapq as hq

def solution(operations):
    queue = []
    for i in operations:
        command, data = i.split(" ")
        if command == 'I':
            hq.heappush(queue, int(data)) 
        elif command == 'D':
            if queue: 
                if data == '1':
                    queue.remove(max(queue)) 
                    hq.heapify(queue) 
                elif data == '-1': 
                    hq.heappop(queue) 
    if not queue: 
        return [0, 0]
    else: 
        return [max(queue), hq.heappop(queue)]   
