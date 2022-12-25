import sys 

n = int(sys.stdin.readline())
subjects = list(map(int, sys.stdin.readline().split()))
new_subjects = n *[0]
max_subject = max(subjects)

for i in range(n):
    new_subjects[i] = subjects[i]/max_subject*100

print(sum(new_subjects)/len(new_subjects))