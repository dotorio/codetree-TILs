N = int(input())
devs = list(map(int, input().split()))
devs.sort()
ball = 0
while devs:
    start = devs.pop()
    if not devs:
        ball += 1
        break
    next = devs.pop()
    min_dis = start - next
    while devs:
        if min_dis > next - devs[-1]:
            break
        min_dis = next - devs[-1]
        next = devs.pop()
    ball += 1
print(ball)