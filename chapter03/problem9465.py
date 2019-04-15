# 스티커

#  상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다.
# 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다. 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.
#
# 상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다.
# 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.

# 각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.

# 풀이방법 : dp
# dp[i][j] = i번째 열에서 j행에 스티커를 뜯는 경우 최대 값
# dp[i][j] = [max(dp[i-1][1],dp[i-2][1]) + sticker[0][i-1], max(dp[i-1][0],dp[i-2][0]) + sticker[1][i-1]]


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

