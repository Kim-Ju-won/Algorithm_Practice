import sys

test_case = sys.stdin

for t in test_case : 
    if len(t) < 2: 
        break
    a, b = tuple(map(int, t.split()))
    print(a+b)


