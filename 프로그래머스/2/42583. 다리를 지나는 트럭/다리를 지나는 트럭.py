from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting_q = deque(truck_weights)  
    simulation_q = deque([0] * bridge_length)  
    bridge_weight = 0  

    while waiting_q or bridge_weight > 0:
        answer += 1
        out = simulation_q.popleft()  
        bridge_weight -= out
        
        if waiting_q:            
            if bridge_weight + waiting_q[0] <= weight:
                truck = waiting_q.popleft()
                simulation_q.append(truck)
                bridge_weight += truck
            else:
                simulation_q.append(0)  
    return answer
