def remainder(a, b, c):
    first = (a+b)%c
    second = ((a%c) + (b%c))%c
    third = (a*b)%c
    fourth = ((a%c) * (b%c))%c
    return first, second, third, fourth

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    
    answer = remainder(a, b, c)
    
    for i in answer:
        print(i)
   
    
