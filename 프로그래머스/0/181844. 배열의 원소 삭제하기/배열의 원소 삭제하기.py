def solution(arr, delete_list):
    delete_set = set(delete_list)
    return [v for i, v in enumerate(arr) if v not in delete_set]