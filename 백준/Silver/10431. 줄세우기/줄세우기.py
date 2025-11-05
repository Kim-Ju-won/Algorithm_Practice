import sys

p = int(sys.stdin.readline())
testcases = [list(map(int, sys.stdin.readline().split())) for _ in range(p)]

for testcase in testcases : 
    number = testcase[0]
    line = testcase[1:]
    count = 0 
    for i in range(1, len(line)):
        for j in range(i,0,-1):
            if line[j-1] > line[j]:
                count += 1
                line[j-1], line[j] = line[j], line[j-1]
    print(number, count)