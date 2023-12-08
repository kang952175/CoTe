def case_comparison(a, b):
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")
    return
        
if __name__ == "__main__":
    a, b = map(int, input().split())
    
    case_comparison(a, b)