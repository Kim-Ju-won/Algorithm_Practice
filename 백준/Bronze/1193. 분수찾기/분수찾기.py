import sys 

n = int(sys.stdin.readline())
count = 0
num = 0
nu = 0
de = 0
while n > num  :
    count+=1
    temp_num = num+count
    if count % 2 == 0 : 
        nu, de = 1, count
    else : 
        nu, de = count, 1
    if num < n <= temp_num:
        for i in range(num+1, temp_num+1):
            if i == n : 
                break
            if count % 2 == 0 : 
                nu += 1
                de -= 1
            else : 
                nu -= 1
                de += 1
    num = temp_num

print(f'{nu}/{de}')
