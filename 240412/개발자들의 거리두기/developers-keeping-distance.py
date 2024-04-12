N = int(input())

# 개발자들의 위치와 감염 여부를 devs 리스트에 담아서 정렬한다
devs = []
for _ in range(N):
    loc, inf = map(int, input().split())
    devs.append((loc, inf))
devs.sort()

# 감염자와 비감염자 간의 최소 거리 dis를 구한다
dis = 10**6
for i in range(N-1):
    if (devs[i][1], devs[i+1][1]) in  [(1,0), (0,1)]: 
        dis = min(dis, devs[i+1][0] - devs[i][0])
        
# 구한 최소 거리-1 을 양수 거리 R로 볼 수 있다
R = dis - 1

# 처음 감염된 개발자 수 inf_devs, devs를 순회할 idx, 감염 중일 때 True로 바꿀 btn
inf_devs, idx, btn = 0, 0, False

# devs를 모두 순회할 때까지
while idx != N:
		# 감염 중이 아니라면
    if not btn:
		    # 감염이 시작됏는지 확인해서
        if devs[idx][1]:
		        # 시작됐다면 버튼을 켜고 감염된 개발자 수를 1 올림
            btn = True           
            inf_devs += 1
    # 감염 중이라면
    else:
		    # 현재 개발자가 감염되었다면
        if devs[idx][1]:
		        # 현재 개발자가 이전 개발자에게 전염될 수 있는가 확인
            if devs[idx][0] - devs[idx-1][0] > R:
		            # 전염될 수 없다면 버튼을 끄고
                btn = False
                # 다음 시작점이 되어야 하기 때문에 idx를 1 내림
                idx -= 1
        # 현재 개발자가 감염되지 않았다면
        else:
		        # 버튼을 끈다
            btn = False
    # 순회를 계속하기 위해 idx를 1 올림
    idx += 1
# 알아낸 처음 감염된 개발자 수를 출력
print(inf_devs)