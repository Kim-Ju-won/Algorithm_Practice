import sys 

n = int(sys.stdin.readline())

for i in range(n):
    count = 0 
    score = 0 
    s = sys.stdin.readline().rstrip()
    for ele in s : 
        if ele == 'O':
            count += 1 
            score += count
        elif ele == 'X':
            count = 0 
    print(score)
