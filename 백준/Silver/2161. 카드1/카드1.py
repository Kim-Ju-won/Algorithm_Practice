import sys
from collections import deque

n = int(sys.stdin.readline())

cards = [ i for i in range(1,n+1)]
cards = deque(cards)

put = True 

while cards : 
    if put : 
        print(cards.popleft(), end=" ")
        put = False
        
    else : 
        cards.append(cards.popleft())
        put = True

    