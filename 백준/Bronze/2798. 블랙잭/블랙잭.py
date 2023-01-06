import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
card = list(map(int, sys.stdin.readline().split()))
card.sort()

sum_card = -1

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] > sum_card and  card[i]+card[j]+card[k] <= m: 
                sum_card = card[i]+card[j]+card[k]

print(sum_card)