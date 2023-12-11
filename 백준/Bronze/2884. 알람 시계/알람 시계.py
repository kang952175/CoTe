def early_alarm(h, m):
    if m < 45 :	 
        if h == 0 :	
            h = 23
            m += 60
        else :	
            h -= 1	
            m += 60
            
    return print(h, m-45)

if __name__ == "__main__":
    h, m = map(int, input().split())
    
    early_alarm(h, m)

