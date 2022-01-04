

import sys

N = int(sys.stdin.readline())

sys.setrecursionlimit(10**9)
#
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    
    A, B = map(int, sys.stdin.readline().split())
    
    tree[A].append(B)
    tree[B].append(A)

parent = [0 for _ in range(N+1)] #visited


def dfs(child, tree, parent):
    for i in tree[child]:
        if parent[i] == 0: # unvisited
            parent[i] = child # parent update
            dfs(i, tree, parent)
            
            
dfs(1, tree, parent)

for i in range(2, N+1):
    print(parent[i])
