import heapq

def sync_heaps(min_heap, max_heap, invalid_entries):
    # 제거된 요소들을 무시하고 힙을 동기화하는 함수
    while min_heap and min_heap[0][1] in invalid_entries:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] in invalid_entries:
        heapq.heappop(max_heap)

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙을 위한 최소 힙 (부호 반전)
    invalid_entries = set()  # 삭제된 요소의 인덱스를 추적하는 집합
    count = 0  # 힙에 있는 요소의 수

    for op in operations:
        command, value = op.split()
        value = int(value)

        if command == 'I':
            heapq.heappush(min_heap, (value, count))
            heapq.heappush(max_heap, (-value, count))
            count += 1
        elif command == 'D':
            if value == 1 and max_heap:  # 최댓값 제거
                while max_heap:
                    val, idx = heapq.heappop(max_heap)
                    if idx not in invalid_entries:
                        invalid_entries.add(idx)
                        break
            elif value == -1 and min_heap:  # 최솟값 제거
                while min_heap:
                    val, idx = heapq.heappop(min_heap)
                    if idx not in invalid_entries:
                        invalid_entries.add(idx)
                        break

    # 최종 동기화
    sync_heaps(min_heap, max_heap, invalid_entries)

    # 결과 반환
    if min_heap and max_heap:
        min_val = min_heap[0][0]
        max_val = -max_heap[0][0]
        return [max_val, min_val]
    else:
        return [0, 0]