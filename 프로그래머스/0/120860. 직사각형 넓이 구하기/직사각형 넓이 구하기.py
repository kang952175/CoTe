import math

def angle(point):
    # 점 (x, y)와 원점 사이의 각도를 계산합니다. 그 결과는 -π에서 π 사이의 값으로 반환
    x, y = point
    return math.atan2(y, x)

def solution(dots):
    # 기준점
    origin = min(dots, key=lambda point: (point[1], point[0]))
    # 원점에서 각 점까지의 각도를 시계 방향으로 계산
    sorted_dots = sorted(dots, 
                         key=lambda point: -angle([point[0]-origin[0], point[1]-origin[1]]))
    
    a, b, c, d = sorted_dots
    answer = abs((b[0]-a[0]) * (c[1]- b[1]))
    
    return answer

