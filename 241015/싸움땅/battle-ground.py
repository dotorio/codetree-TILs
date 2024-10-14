from heapq import heappop, heappush

n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
p_area = [[-1]]
players = []
for _ in range(m):
    players.append(list(map(int, input().split())))
points = [0]*m

def go(player):
    global area
    pass

def fight()

for _ in range(k):
    for i in range(m):
        go(players[i])
print(*points)