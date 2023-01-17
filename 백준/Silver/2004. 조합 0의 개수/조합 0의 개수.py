import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
m = min(m, n-m)

def comb_count_zero(n):
    count = {
        2:0, 5:0
    }
    check_5 = n
    while check_5 > 0 : 
        check_5//=5 
        count[5]+=check_5
    check_2 = n
    while check_2 > 0 : 
        check_2//=2
        count[2]+=check_2

    return count
x,y =comb_count_zero(n).values()
for ele in [n-m,m]:
    i,j= comb_count_zero(ele).values()
    x-=i
    y-=j
print(min(x,y))

