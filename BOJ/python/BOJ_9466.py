
import sys

T = int(sys.stdin.readline())



def dfs(X):
    global result
    student[X] = True
    cycle.append(X)
    pick = picks[X-1]
    
    if student[pick]:
        if pick in cycle:
            result += cycle[cycle.index(pick):]
        return
    else:
        dfs(pick)
        

for _ in range(T):

    N = int(sys.stdin.readline())

    picks = list(map(int,sys.stdin.readline().strip().split()))
    
    student = [False] * (N+1)
    result = []
    
    for i in range(1, N+1):
        if not student[i]:
            cycle = []
            dfs(i)
            
    print(N - len(result))