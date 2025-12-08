# 카드 구매하기 
# 스타트링크에서 만든 PS 카드 모으기 
# PS 분야의 유명한 사람들의 아이디와 얼굴이 적혀있는 카드 
# 각각의 카드에는 등급을 나타내는 색이 칠해져 있다. 

# 전설카드, 레드카드, 오렌지카드, 퍼플카드, 블루카드, 청록카드, 그린카드, 그레이 카드

# 카드는 카드팩 구매 -> 1...N개가 포함된카드 존재 

# 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급 카드가 많이 들어있을 것 
# 민규는 돈을 최대한 많이 지불 -> 카드 N개 구입 
# 중복으로 된 카드 종류를 구매 가능 

# 카드 팩이 주어졌을 때 민규가 구매해야하는 최댓값 
# 1<=N <=1000, 1<=Pn<1000

import sys

n = int(sys.stdin.readline())
cards = [0]+list(map(int, sys.stdin.readline().split()))
DP = [ 0 for _ in range(n+1)]

for i, card in enumerate(cards) : 
    if i <= n : 
        DP[i] = card 
        
for i in range(n+1):
    for j, card in enumerate(cards) : 
        if i-j >=0 : 
            DP[i] = max(DP[i], DP[i-j] + card)

print(DP[-1])