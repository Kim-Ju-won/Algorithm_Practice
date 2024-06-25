import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
total = [0 for _ in range(10)]
species = 1
total[arr[0]] = 1
total_sum = 1
j = 1

if len(set(arr)) >= 3:
    for i in range(n):
        while species <= 2 and j <= n - 1:

            total[arr[j]] += 1
            total_sum += 1
            if total[arr[j]] == 1:
                species += 1
            if species <= 2:
                answer = max(answer, total_sum)
            j += 1

        total[arr[i]] -= 1
        total_sum -= 1
        if total[arr[i]] == 0:
            species -= 1

    print(answer)
else:
    print(len(arr))
