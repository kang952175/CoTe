def oven_timer(h, m, t):
    h += t // 60
    m += t % 60
    
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    return print(h, m)

if __name__ == "__main__": 
    h, m = map(int, input().split())
    t = int(input()) 

    oven_timer(h, m, t)