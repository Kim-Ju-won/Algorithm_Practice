import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
def comb(n,m,k,temp):
    if len(temp)==m:
        for ele in temp : 
            print(ele, end=' ')
        print()
    else : 
        for i in range(k,n):
            temp.append(arr[i])
            comb(n,m,i,temp)
            temp.pop()

comb(n,m,0,[])