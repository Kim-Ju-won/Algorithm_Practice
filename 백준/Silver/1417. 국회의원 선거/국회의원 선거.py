import sys

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]
            
dasom = arr[0]
candidates = arr[1:]
diff = 0 
count = 0 
need_buy = False
candidates.sort(reverse=True)

for candidate in candidates: 
    if dasom <= candidate : 
        need_buy = True
        break

buy = 0 
while need_buy :
    if candidates[0] >= dasom : 
        dasom += 1
        candidates[0] -= 1
        buy += 1
    else : 
        need_buy = False
        break 
    
    candidates.sort(reverse=True)
        
print(buy)