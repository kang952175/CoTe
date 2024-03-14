def solution(array):    
    sorted_array = sorted(array)
    n = len(sorted_array)

    if n % 2 == 1:    
        return sorted_array[n // 2]
    else:
        return (sorted_array[(n // 2) - 1] + sorted_array[n // 2]) / 2
