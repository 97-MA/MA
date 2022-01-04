import sys

sys.setrecursionlimit(9999)

def dfs(A):
    visited[A] = True
    for e in  L[A]:
        if not visited[e]:
            dfs(e)



N , M =  map(int, sys.stdin.readline().split())

L = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    L[A].append(B)
    L[B].append(A)

for j in range(1, N+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
