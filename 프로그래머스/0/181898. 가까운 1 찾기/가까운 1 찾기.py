def solution(arr, idx):
    answer = -1
    if 1 in arr[idx:]:
        print(arr[idx:])
        answer = arr[idx:].index(1)+idx
    return answer