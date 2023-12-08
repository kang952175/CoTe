def grade(x):
    if 90 <= x <= 100:
        return "A" 
    elif 80 <= x <= 89:
        return "B"
    elif 70 <= x <= 79:
        return "C"
    elif 60 <= x <= 69:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    x = int(input())
    answer = grade(x)
    print(answer)