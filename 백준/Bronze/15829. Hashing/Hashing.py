import sys 

def hash(s,n):
    ans = 0 
    for i in range(n):
        ans+=(ord(s[i])-96)*(31**i)
    return ans%1234567891

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
print(hash(s,n))