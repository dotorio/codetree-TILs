N = int(input())
devs = list(map(int, input().split()))
devs.sort()
ball, dir, idx = 0, 0, 0
while True:
    start = devs[idx]
    idx += 1
    if idx == N:
        ball += 1
        break    
    next = devs[idx]
    dist = next - start
    
    idx += 1
    while idx != N:
        if not dir:
            if dist <= devs[idx] - next:
                dir = 1                
            else:
                dir = 2
            dist = devs[idx] - next
            
            next = devs[idx]
            idx += 1
        elif dir == 1:
            if dist > devs[idx] - next:
                idx -= 1
                break
            dist = devs[idx] - next
            
            next = devs[idx]
            idx += 1
        else:
            if dist <= devs[idx] - next:
                
                break
            dist = devs[idx] - next
            
            next = devs[idx]
            idx += 1
    ball += 1
    if idx == N:
        break
    dir = 0

print(ball)