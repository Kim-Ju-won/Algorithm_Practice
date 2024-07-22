import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

eat = []
wait = []

for i in range(n):
    if arr[i] != len(eat) + 1:
        while wait:
            if wait[-1] == len(eat) + 1:
                eat.append(wait.pop())
            else:
                break
        wait.append(arr[i])
    else:
        eat.append(arr[i])


while wait:
    if wait[-1] == len(eat) + 1:
        eat.append(wait.pop())
    else:
        break

print("Sad" if wait else "Nice")
