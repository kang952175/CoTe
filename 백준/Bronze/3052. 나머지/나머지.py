remainder_set = set() 

for _ in range(10):
    num = int(input())
    remainder = num % 42  
    remainder_set.add(remainder) 

print(len(remainder_set))  
