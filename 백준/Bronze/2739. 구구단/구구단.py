def times_table(N):
    for i in range(1,10):
        print(f"{N} * {i} = {N * i}")
    
if __name__ == "__main__":
    N = int(input())
    times_table(N)