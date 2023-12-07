def Arithmetic(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    quotient = a // b
    remainder = a % b
    
    return add, sub, mul, quotient, remainder

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    answer = Arithmetic(a, b)
    
    for i in answer:
        print(i)
    
