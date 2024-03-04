from statistics import mean

N = int(input())
M = list(map(int, input().split()))

max_num = max(M)
for i in range(len(M)):   
    M[i] = M[i]/max_num * 100

print(mean(M)) 
