def is_leap_year(x):
    if x % 400 == 0:
        return 1
    elif x % 4 == 0 and x % 100 !=  0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    x = int(input())
    answer = is_leap_year(x)
    print(answer)