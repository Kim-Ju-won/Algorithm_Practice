import sys 

students = 30*[0]

for i in range(28):
    submit = int(sys.stdin.readline())
    students[submit-1]-=1

for i in range(len(students)):
    if students[i] ==0 : 
        print(i+1)
