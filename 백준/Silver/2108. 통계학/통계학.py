import sys

n =int(sys.stdin.readline())
arr = []
arr_dict = dict()
for i in range(1,n+1):
    ele = int(sys.stdin.readline())
    arr.append(ele)
    if ele in arr_dict : 
        arr_dict[ele]+=1
    else : 
        arr_dict[ele]=1
arr.sort()
print(round(sum(arr)/len(arr)))
print(arr[n//2])
hash_dict = dict()
for key in arr_dict : 
    if arr_dict[key] in hash_dict : 
        hash_dict[arr_dict[key]].append(key)
    else : 
        hash_dict[arr_dict[key]]=[key]
keys = list(hash_dict.keys())
keys.sort()
ans = hash_dict[keys[-1]]
ans.sort()
if len(ans) > 1 : 
    print(ans[1])
else : 
    print(ans[0])
print(abs(arr[-1]-arr[0]))