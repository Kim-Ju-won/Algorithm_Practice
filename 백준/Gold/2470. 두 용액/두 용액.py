import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
plus = []
minus = []
min_num = sys.maxsize
min_list=[-1,-1]

for ele in arr : 
    if ele >= 0 :
        plus.append(ele)
    else : 
        minus.append(ele)
plus.sort()
minus.sort()

if len(plus) >= 2 and len(minus) >= 2 : 
    if abs(plus[0]+plus[1]) < abs(minus[-1] + minus[-2]) : 
        min_num =abs(plus[0]+plus[1]) 
        min_list = [plus[0], plus[1]]
    else : 
        min_num =abs(minus[-1] + minus[-2])
        min_list =[ minus[-2], minus[-1]]
elif len(plus) >=2 : 
    min_num =abs(plus[0]+plus[1]) 
    min_list = [plus[0], plus[1]]
elif len(minus) >= 2 : 
    min_num =abs(minus[-1] + minus[-2])
    min_list =[ minus[-2], minus[-1]]

j = len(plus)-1
if len(minus) >= 1 and len(plus) >= 1 : 
    for i in range(len(minus)) : 
        check = abs(minus[i]+plus[j])
        check_list = [minus[i],plus[j]]
        while j > 0 : 
            j-=1 
            if abs(minus[i]+plus[j]) >= check :
                j+=1
                break 
            else : 
                check = abs(minus[i]+plus[j])
                check_list = [minus[i],plus[j]]
        if check < min_num : 
            min_num = check 
            min_list = check_list 

for ele in min_list : 
    print(ele, end=' ')