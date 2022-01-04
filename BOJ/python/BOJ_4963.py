import sys

sys.setrecursionlimit(10**4) 






        

def dfs(x, y):
    
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    
    visited[x][y]=True
    
    
    # world[x][y]=0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<W and 0<=ny<H:
            if world[nx][ny]==1 and not visited[nx][ny]:
                dfs(nx,ny)
while True:
    H, W = map(int,sys.stdin.readline().split())
    if W == H == 0:
        break
    world = [[] for _ in range(W)]
    
    for i in range(W):
        world[i] = list(map(int, sys.stdin.readline().split()))
        
    visited = [[False for _ in range(H)] for _ in range(W)]
    
        
    count = 0
    for y in range(H):
        for x in range(W):
            
            if not visited[x][y] and world[x][y] == 1:
                
                dfs(x,y)
                count += 1

    
    print(count)