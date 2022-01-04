
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
queue = deque([])
dx, dy = [-1,1,0,0],[0,0,-1,1]
res = 0

for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            queue.append([x,y])
            
def bfs():
    while queue:
        print(queue)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx,ny])
                print(box)
                
bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)
                