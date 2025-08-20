import sys

n = int(sys.stdin.readline())
if n != 0:
    arr = list(map(int, sys.stdin.readline().split()))
    sum_arr = 0
    expectation = 0
    distribution = dict()

    for ele in arr:
        sum_arr += ele
        if ele not in distribution:
            distribution[ele] = 1
        else:
            distribution[ele] += 1

    print(
        f"{round((sum_arr / n) / (sum([(x * y / n) for x, y in distribution.items()])), 3):.2f}"
    )
else:
    print("divide by zero")
