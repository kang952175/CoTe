N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]  

for _ in range(M):
    st, end = map(int, input().split())
    st -= 1  
    basket = basket[:st] + basket[st:end][::-1] + basket[end:]

print(' '.join(map(str, basket)))  
