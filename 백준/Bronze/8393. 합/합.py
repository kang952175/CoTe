def sigma(n):
    output = 0
    for i in range(1,n + 1):
        output += i
    return output

if __name__ == "__main__":
    n = int(input())
    output = sigma(n)
    print(output)