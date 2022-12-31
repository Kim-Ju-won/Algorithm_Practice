import sys 

n = int(sys.stdin.readline())
group_cnt = 0 
for i in range(n):
    check=True
    g_dict = dict()
    s = sys.stdin.readline().rstrip()
    for j in range(len(s)) : 
        if j == 0 : 
            g_dict[s[j]] = 1
        else : 
            if s[j] != s[j-1]:
                if s[j] not in g_dict : 
                    g_dict[s[j]] = 1
                else : 
                    check = False
                    break
    if check == True : 
        group_cnt += 1

print(group_cnt)
