def mul_three_digit_numbers(a, b):
    hundred, ten, unit = int(str(b)[0]), int(str(b)[1]), int(str(b)[2]) 
    unit = a * unit
    ten = a * ten
    hundred = a * hundred
    result = ( hundred * 100) + ( ten * 10) + (unit)
    return unit, ten, hundred, result

if __name__ == "__main__":
    a = int(input())
    b = int(input())

    answer = mul_three_digit_numbers(a, b)
    
    for i in answer:
        print(i)