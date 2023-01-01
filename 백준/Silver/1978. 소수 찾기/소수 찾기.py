import sys

def solution(ele):
    count = 0 
    if ele == 1: 
        return False
    for i in range(2,int(ele**0.5)+1):
        if ele % i == 0 : 
            count += 1
        if count >= 1 : 
            return False
    return True

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = 0 
for ele in arr: 
    if solution(ele) :
        count+=1 

print(count)