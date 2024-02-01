import sys

n, y, w = sys.stdin.readline().split()
while (n, y, w) != ("#", "0", "0"):

    if int(y) > 17 or int(w) >= 80:
        print(f"{n} Senior")
    else:
        print(f"{n} Junior")

    n, y, w = sys.stdin.readline().split()
