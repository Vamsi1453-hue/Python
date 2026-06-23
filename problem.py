from collections import deque
def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    dist = [[float('inf')] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist
mat1 = [[0,0,0],[0,1,0],[0,0,0]]
mat2 = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat1))
print(updateMatrix(mat2))
