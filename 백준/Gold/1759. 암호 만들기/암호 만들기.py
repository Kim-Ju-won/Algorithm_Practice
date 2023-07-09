import sys
from itertools import combinations as comb

n, m = tuple(map(int, sys.stdin.readline().split()))
candidates = sys.stdin.readline().split()
vowel_set = {"a", "i", "e", "o", "u"}
vowels = []
consonants = []
for c in candidates:
    if c not in vowel_set:
        consonants.append(c)
    else:
        vowels.append(c)
v_n, c_n = len(vowels), len(consonants)
ans = []
for i in range(1, v_n + 1):
    for j in range(2, c_n + 1):
        if i + j == n:
            for v in list(comb(vowels, i)):
                for c in list(comb(consonants, j)):
                    ans.append("".join(sorted(list(v) + list(c))))
        elif i + j > n:
            break
ans.sort()
for ele in ans:
    print(ele)