import sys

s = sys.stdin.readline().rstrip()
s_dict = dict()

for c in s:
    if c in s_dict:
        s_dict[c] += 1
    else:
        s_dict[c] = 1

palindrome_dict = dict()

for key, num in s_dict.items():
    if num in palindrome_dict:
        palindrome_dict[num].append(key)
    else:
        palindrome_dict[num] = [key]

checker = True
odd_checker = ""
if len(s) % 2 == 0:
    for k in palindrome_dict.keys():
        if k % 2 == 1:
            checker = False
            break
else:
    temp_odd = 1
    for k in palindrome_dict.keys():
        if k % 2 == 1:
            temp_odd -= len(palindrome_dict[k])
            if temp_odd == 0:
                odd_checker = palindrome_dict[k][-1]
            if temp_odd < 0:
                checker = False
                break


if checker:
    keys = sorted(s_dict.keys())

    answer = ""
    for k in keys:
        answer += k * (s_dict[k] // 2)
    if len(s) % 2 == 1:
        answer += odd_checker
    for k in keys[::-1]:
        answer += k * (s_dict[k] // 2)
    print(answer)

else:
    print("I'm Sorry Hansoo")
