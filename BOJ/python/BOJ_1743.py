
from collections import deque
import sys

N, M, K = map(int, sys.stdin.readline().split())

path = [[0] * M for _ in range(N)]

visited = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    path[r-1][c-1] = 1
    
dx = [ -1 ,1 ,0, 0 ]
dy = [ 0, 0, -1, 1]

queue = deque()
def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and path[nx][ny]==1:
                queue.append([nx,ny])
                visited[nx][ny]=1
                cnt += 1
    return cnt

result = 0           

for i in range(N):
    for j in range(M):
        if path[i][j] == 1:
            
            result = max(result, bfs(i,j))
            
print(result)