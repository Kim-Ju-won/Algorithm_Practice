import sys

number = sys.stdin.readline().rstrip()
num_dict = dict()
for i in range(10):
    num_dict[str(i)] = 0

for n in number:
    num_dict[str(n)] += 1

max_num = 0
for i in range(10):
    if i != 6 and i != 9:
        max_num = max(num_dict[str(i)], max_num)
check = (
    (num_dict["6"] + num_dict["9"]) // 2
    if (num_dict["6"] + num_dict["9"]) % 2 == 0
    else (num_dict["6"] + num_dict["9"]) // 2 + 1
)
max_num = max(check, max_num)
print(max_num)
