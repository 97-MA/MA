import sys

N = int(sys.stdin.readline())

save_ls = [0]*N


ls = list(map(int,sys.stdin.readline().split()))

save_ls[0] = ls[0]


if N == 1:
    print(save_ls[0])
    exit()
else:
    for i in range(1,N):
        if save_ls[i-1] + ls[i] >= save_ls[i]:
            save_ls[i] = save_ls[i-1] + ls[i]
        else:
            save_ls[i] = ls[i]
# print(save_ls)

print(max(save_ls))