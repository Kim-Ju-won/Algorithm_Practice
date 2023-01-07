import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
pocketmon_name_dict = dict()
pocketmon_num_dict = dict()

for i in range(n):
    pocketmon_name= sys.stdin.readline().rstrip()
    pocketmon_name_dict[pocketmon_name] = (i+1)
    pocketmon_num_dict[i+1] = pocketmon_name


for _ in range(m):
    check = sys.stdin.readline().rstrip()
    if '0'<=check[0]<='9':
        print(pocketmon_num_dict[int(check)])
    else : 
        print(pocketmon_name_dict[check])
