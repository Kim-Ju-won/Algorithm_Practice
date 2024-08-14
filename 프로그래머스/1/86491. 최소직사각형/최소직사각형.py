def solution(sizes):
    max_x, max_y = 0, 0
    for size in sizes : 
        x, y = size 
        if max(max_x, x) * max(max_y, y) < max(max_x, y) * max(max_y, x):
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        else : 
            max_x = max(max_x, y)
            max_y = max(max_y, x)
    return max_x * max_y