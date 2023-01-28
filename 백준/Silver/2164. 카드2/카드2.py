import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque(range(1,n+1))

count = 0 
while len(card) > 1 : 
    if count == 0 : 
        card.popleft()
        count+=1
    else : 
        card.append(card.popleft())
        count-=1
print(card[-1])