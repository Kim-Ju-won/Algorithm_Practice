import sys 
import math 

n = int(sys.stdin.readline())

for i in range(n):
    students = list(map(int, sys.stdin.readline().split()))
    avg = sum(students[1:])/students[0]
    count = 0
    for ele in students[1:]:
        if ele > avg : 
            count += 1 
    percent = count / students[0] * 1000000
    if percent % 10 >= 5 : 
        percent = percent//10 + 1
    else : 
        percent = percent//10
    print(f'{percent*0.001:.3f}%')

