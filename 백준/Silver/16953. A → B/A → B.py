import sys

start, end = tuple(map(int, sys.stdin.readline().split()))
count = 0
while start <= end:
    if start == end:
        break
    if end % 2 == 0:
        end //= 2
    elif end % 10 == 1:
        end = int(str(end)[:-1])
    else:
        break
    count += 1
print(count + 1 if start == end else -1)
