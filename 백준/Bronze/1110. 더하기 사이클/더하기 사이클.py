n = input()
check = n
count = 0
while True : 
    if len(n) == 1 : 
        n = '0'+n 
    n = n[1]+str((int(n[0])+int(n[1]))%10)
    count += 1
    if int(check) == int(n) :
        break
print(count)