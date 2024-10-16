from heapq import heappush, heappop, heapify

n, m, k = map(int, input().split())
area = [[] for _ in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    nums = [-num for num in nums]
    for j in nums:
        s_area = [j]
        heapify(s_area)
        area[i].append(s_area)
p_area = [[-1]*n for _ in range(n)]
players = dict()
p_loc = dict()
for i in range(m):
    x, y, d, s = map(int, input().split())
    p_area[x-1][y-1] = i
    players[i] = [d, s, 0]
    p_loc[i] = [x-1, y-1]
scores = [0]*m

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(idx):
    global area, p_area, players, p_loc
    x, y = p_loc[idx]
    if 0 <= x + dx[players[idx][0]] < n and 0 <= y + dy[players[idx][0]] < n:
        pass
    else:
        players[idx][0] = (players[idx][0] + 2) % 4
    p_area[x][y] = -1
    x, y = x + dx[players[idx][0]], y + dy[players[idx][0]]   
    p_loc[idx] = [x, y]
    if p_area[x][y] >= 0:
        p2 = p_area[x][y]
        # print(idx, p2)
        if battle(idx, p2):
            lose(p2)
            p_area[x][y] = idx
            gun_change(idx)
        else:
            lose(idx)
            gun_change(p2)
    else:
        p_area[x][y] = idx
        p_loc[idx] = [x, y]
        gun_change(idx)

def battle(p1, p2):
    global scores
    sum_p1, sum_p2 = sum(players[p1][1:]), sum(players[p2][1:])
    if sum_p1 > sum_p2:
        scores[p1] += sum_p1 - sum_p2
        return True
    elif sum_p1 < sum_p2:
        scores[p2] += sum_p2 - sum_p1
        return False
    else:
        if players[p1][1] > players[p2][1]:
            return True
        else:
            return False

def lose(idx):
    global players, p_loc, p_area
    can_move = True
    x, y = p_loc[idx]
    heappush(area[x][y], -players[idx][2])
    players[idx][2] = 0
    while can_move:
        if 0 <= x + dx[players[idx][0]] < n and 0 <= y + dy[players[idx][0]] < n and p_area[x + dx[players[idx][0]]][y + dy[players[idx][0]]] == -1:
            can_move = False
            x, y = x + dx[players[idx][0]], y + dy[players[idx][0]]
            p_loc[idx] = [x, y]
            p_area[x][y] = idx
            gun_change(idx)
        else:
            players[idx][0] = (players[idx][0]+1)%4

def gun_change(idx):
    x, y = p_loc[idx]
    if area[x][y]:
        gun = -heappop(area[x][y])
        # print(gun)
        if players[idx][2] < gun:
            heappush(area[x][y], -players[idx][2])
            players[idx][2] = gun
        else:
            heappush(area[x][y], -gun)

for _ in range(k):
    for idx in range(m):
        go(idx)

print(*scores)