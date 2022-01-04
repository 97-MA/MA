
from collections import deque

import sys

N, M= map(int,sys.stdin.readline().split())

friend = [ [] for _ in range(N+1)]



for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    friend[A].append(B)
    friend[B].append(A)



def bfs(x):
    queue = deque()
    queue.append(x)
    bacon=[0]*(N+1)
    visited = [x]
    
    while queue:
        pop = queue.popleft()
        for i in friend[pop]:
            if i not in visited:
                
                bacon[i] = bacon[pop] + 1
                visited.append(i)
                queue.append(i)
                
                
    return(sum(bacon))
                        
a = []                    
for i in range(1,N+1):
    a.append(bfs(i))
print(a.index(min(a))+1)