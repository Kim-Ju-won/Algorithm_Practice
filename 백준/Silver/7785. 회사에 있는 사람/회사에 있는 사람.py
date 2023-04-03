import sys

n = int(sys.stdin.readline())
enter_dict = dict()

for _ in range(n):
    person, log = sys.stdin.readline().split()
    if log == 'enter':
        enter_dict[person] = 1
    else : # leave
        enter_dict[person] = 0

keys = list(enter_dict.keys())
keys.sort(reverse=True)

for key in keys : 
    if enter_dict[key] == 1 : 
        print(key)