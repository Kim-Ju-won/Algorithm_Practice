# 오르막수
# 수의 자리가 오름차순을 이루는 수 
# 인접한 수가 같아도 오름차순 
# 2234, 3678 
# 2232, 911
# x

# 입력 : N (1 <= N <= 1000) => 자릿수 : 따라서 
# N의 오르막 개수 

# 숫자가 커지는걸 그대로 구하면 안됨. 바로 문제가 시간 오류 
# 3의 자리 숫자는 1의 자리가, 1의 자리 숫자는 0의 자리 갯수가 필요 
# 결과를 10007로 나눈 나머지를 저장해줘, 너무 커지는 것을 막음 

import sys

n = int(sys.stdin.readline())

DP = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(n):
    for j in range(10):
        if i == 0 : 
            DP[i][j] = 1
        else : 
            for k in range(j, 10):
                DP[i][j] += DP[i-1][k]
                



print(sum(DP[n-1])%10007)