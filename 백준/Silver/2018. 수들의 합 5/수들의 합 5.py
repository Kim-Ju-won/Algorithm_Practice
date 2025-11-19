N = int(input())
ans = 0
for i in range(1,N+1):
    # 짝수개일 경우 소숫점자리 0.5면 됨
    if i % 2 == 0:
        if (N/i - N//i) == 0.5:
            if N/i + 0.5 > i/2:
                ans += 1
    # 홀수개일 경우 나누어떨어지는지 보면 됨.
    else:
        if N % i == 0:
            # N//i는 중간 값
            # i//2+1은 중간 값의 인덱스(+1)
            if N//i > (i//2):
                ans += 1

print(ans)