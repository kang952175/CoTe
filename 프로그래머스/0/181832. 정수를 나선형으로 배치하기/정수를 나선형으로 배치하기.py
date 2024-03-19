def solution(n):
    matrix = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, direction = 0, 0, 0

    for value in range(1, n**2 + 1):
        matrix[x][y] = value

        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            direction = (direction + 1) % 4 
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny
        
    return matrix
