def solution(arr, L):
    for i in range(len(arr)):
        if arr[i] < L:
            print(arr[i], end= " ")
    
if __name__ == "__main__":
    N, L = map(int, input().split())
    arr = list(map(int, input().split()))
    solution(arr, L)
    