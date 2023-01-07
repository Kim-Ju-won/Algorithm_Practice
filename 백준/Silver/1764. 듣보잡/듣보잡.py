import sys 

n, m =tuple(map(int, sys.stdin.readline().split()))
p_dict = dict()
answer = []
for _ in range(n+m):
    p = sys.stdin.readline().rstrip()
    if p in p_dict : 
        p_dict[p] += 1
        answer.append(p)
    else : 
        p_dict[p] = 1

answer.sort()
print(len(answer))
for ele in answer : 
    print(ele)