# n = int(input())
# seq1 = [0] + list(map(int, input().split()))
# seq2 = [0] * (n+1)
# seq3 = [0] * (n+1)

# for i in range(1, n+1):

from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(dp))