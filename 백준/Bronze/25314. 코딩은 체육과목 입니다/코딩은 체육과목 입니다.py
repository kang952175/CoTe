def data_structure(N):
    count = N // 4
    result = ""
    for i in range(1, count + 1):
        result = "long " * i + "int"
    print(result)
    
if __name__ == "__main__":
    n = int(input())
    data_structure(n)