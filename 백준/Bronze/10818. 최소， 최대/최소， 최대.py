def solution(arr):
    print(min(arr), max(arr))
    
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    solution(arr)