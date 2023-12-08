def add_triple_digits(a, b, c):
    return a + b + c

if __name__=="__main__":
    a, b, c = map(int, input().split(' '))
    
    answer = add_triple_digits(a, b, c)
    
    print(answer)