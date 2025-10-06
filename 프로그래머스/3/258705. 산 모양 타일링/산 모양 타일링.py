def solution(n, tops):
    MOD = 10007
    a, b, c, d = [0] * n, [0] * n, [0] * n, [0] * n
    for i in range(n):
        if i == 0:
            a[i], b[i], c[i], d[i] = 1, 1, 1, 1
            if tops[0] == 0:
                d[i] = 0
            continue
        
        a[i] = (a[i-1] + b[i-1] + c[i-1] + d[i-1]) % MOD
        b[i] = (a[i-1] + b[i-1] + d[i-1]) % MOD
        c[i] = (a[i-1] + b[i-1] + c[i-1] + d[i-1]) % MOD
        d[i] = (a[i-1] + b[i-1] + c[i-1] + d[i-1]) % MOD
        
        if tops[i] == 0:
                d[i] = 0

    answer = a[-1] + b[-1] + c[-1] + d[-1]
    return answer % MOD