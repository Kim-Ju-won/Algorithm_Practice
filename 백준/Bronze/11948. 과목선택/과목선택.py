import sys

choose_3 = []
choose_1 = []

for _ in range(4):
    choose_3.append(int(sys.stdin.readline()))

for _ in range(2):
    choose_1.append(int(sys.stdin.readline()))

choose_3.sort(reverse=True)
choose_1.sort(reverse=True)
print(sum(choose_3[:3])+choose_1[0])
