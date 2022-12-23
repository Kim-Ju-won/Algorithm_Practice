import sys 

h, m = tuple(map(int, sys.stdin.readline().split()))
time = int(sys.stdin.readline())
time_h = time//60
time_m = time%60

if m+time_m >= 60 : 
    time_h +=1

print((h+time_h)%24, (m+time_m)%60)