import sys

t = int(sys.stdin.readline())
def fall(n,l,k,ant):
    ant_remains = []
    check_list = []
    for i in range(n):
        if ant[i][1] > 0 : 
            ant_remains.append([l-ant[i][0],ant[i][1]])
            check_list.append('+')
        else : 
            ant_remains.append([ant[i][0],ant[i][1]])
            check_list.append('-')
    minus = []
    plus = []
    new_remains = []
    for i in range(n) : 
        if check_list[i] == '-':
            minus.append(ant_remains[i][0])
        else : 
            plus.append(ant_remains[i][0])
    new_remains = minus + plus
    for i in range(n):
        ant_remains[i][0] = new_remains[i]
    ant_remains.sort(key=lambda x : (x[0],x[1]))
    return ant_remains[k-1][1]

for _ in range(t):
    n, l, k = tuple(map(int, sys.stdin.readline().split()))
    ant = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(fall(n,l,k,ant))