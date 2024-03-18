def transform(arr):
    new_arr = []
    for n in arr:
        if n >= 50 and n % 2 == 0:
            new_arr.append(n // 2)
        elif n < 50 and n % 2 != 0:
            new_arr.append(n * 2 + 1)
        else:
            new_arr.append(n)
    return new_arr

def solution(arr):
    count = 0
    while True:
        prev_arr = arr[:]
        arr = transform(arr)
        if arr == prev_arr:
            return count  
        count += 1

