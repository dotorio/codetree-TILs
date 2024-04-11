N = int(input())
devs = list(map(int, input().split()))
devs.sort()
ball, btn = 0, 0
while devs:
    start = devs.pop()
    if not devs:
        ball += 1
        break
    next = devs.pop()
    dis = start - next
    while devs:
        if not btn:
            next2 = devs[-1]
            if dis < next - next2:
                # 오름차순
                btn = 1            
            else:
                # 내림차순
                btn = 2
            dis = next - next2
            next = devs.pop()
        elif btn == 1:
            next2 = devs[-1]
            if dis >= next - next2:
                break
            dis = next - next2
            next = devs.pop()
        else:
            next2 = devs[-1]
            if dis < next - next2:
                break
            dis = next - next2
            next = devs.pop()            
    ball += 1
print(ball)