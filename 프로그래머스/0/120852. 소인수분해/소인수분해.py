import math
def sieve(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

def solution(n):
    answer = set()
    remainder = n
    primes = sieve(n)

    for i in range(2, n +1):
        if primes[i] and remainder % i == 0:
            while remainder % i == 0: 
                remainder = remainder // i
                answer.add(i)

    return sorted(list(answer)) 
