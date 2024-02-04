def solution(arr, v):
    print(arr.count(v))

if __name__ == "__main__":
    N = int(input()) 
    arr = list(map(int, input().split()))
    V = int(input())
    solution(arr, V)
    