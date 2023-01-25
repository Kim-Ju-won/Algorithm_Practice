import sys 

city_n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

min_price = sys.maxsize 
ans = 0

for i in range(city_n-1):
    if min_price > price[i] : 
        min_price = price[i]
    ans += min_price*road[i]
print(ans)