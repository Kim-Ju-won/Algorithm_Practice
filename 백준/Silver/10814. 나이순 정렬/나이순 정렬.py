import sys

n =int(sys.stdin.readline())
ans = []
for i in range(n) :     
    age, name = sys.stdin.readline().split()
    age = int(age)
    ans.append((i,age,name))
ans.sort(key=lambda x : (x[1],x[0]))

for ele in ans : 
    print(ele[1], ele[2])
    