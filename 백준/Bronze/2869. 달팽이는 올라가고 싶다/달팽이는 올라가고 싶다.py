import sys

a, b, v = list(map(int, sys.stdin.readline().split()))
ans = (v-a)//(a-b)+1
print( ans+1 if (v-a)%(a-b) != 0 else ans)