N = int(input())
devs = []
for _ in range(N):
    loc, inf = map(int, input().split())
    devs.append((loc, inf))
devs.sort()
dis = 10**6
for i in range(N-1):
    if (devs[i][1], devs[i+1][1]) in  [(1,0), (0,1)]: 
        dis = min(dis, devs[i+1][0] - devs[i][0])
inf_dis = dis - 1
inf_dev = 0
idx, btn = 0, False
while idx != N:
    if not btn:
        if devs[idx][1]:
            btn = True
            inf_dev += 1
    else:
        if devs[idx][1]:
            if devs[idx][0] - devs[idx-1][0] > inf_dis:
                btn = False
        else:
            btn = False
    idx += 1
print(inf_dev)