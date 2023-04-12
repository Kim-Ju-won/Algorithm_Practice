import sys

def comb(n, m, temp, arr_dict):
    if len(temp) == m :
        for i in range(m):
            print(temp[i], end=' ')
        print()
        return 
    else : 
        for key in arr_keys:
            if arr_dict[key] == 1 : 
                temp.append(key)
                arr_dict[key] = 0 
                comb(n, m, temp, arr_dict)
                arr_dict[key] = 1
                temp.pop()

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
arr_dict = dict()
for ele in arr :
    arr_dict[ele] = 1
arr_keys= list(arr_dict.keys())
arr_keys.sort()
comb(n,m,[],arr_dict)