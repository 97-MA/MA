

import sys

N, M, V = map(int,sys.stdin.readline().split())

visited = [False for _ in range(N+1)]

graph = [ [] for _ in range(N+1)]



for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)
    

for e in graph:
    e.sort()

def dfs(i):
    visited[i] = True
    print(i, end=' ')
    for a in graph[i]:
        if not visited[a]:
            dfs(a)
    
    
from collections import deque

def bfs():
    queue = deque([V])
    visited_b = [False for _ in range(N+1)]
    visited_b[V] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited_b[i]:
                visited_b[i] = True
                queue.append(i)
                
dfs(V)
print()
bfs()
