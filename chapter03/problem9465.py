# 각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.
import sys
f = sys.stdin
n = int(f.readline())

for i in range(n):
    k = int(f.readline())
    sticker = []
    for num in range(2): sticker.append([int(i) for i in f.readline().split()])

    dp = []
    dp.append(0)
    for j in range(1, k+1):
        if   j == 1: dp.append([sticker[0][0], sticker[1][0]])
        elif j == 2: dp.append([sticker[1][0]+sticker[0][1], sticker[0][0]+sticker[1][1]])
        else:
            dp.append([max(dp[j-1][1],dp[j-2][1]) + sticker[0][j-1], max(dp[j-1][0],dp[j-2][0]) + sticker[1][j-1]])
    print(max(dp[k]))

