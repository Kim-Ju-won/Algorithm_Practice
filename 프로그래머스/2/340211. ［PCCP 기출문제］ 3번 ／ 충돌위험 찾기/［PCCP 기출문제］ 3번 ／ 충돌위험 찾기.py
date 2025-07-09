import sys 

def solution(points, routes):
    time_checker = [[] for _ in range(len(routes))]
    
    for idx, route in enumerate(routes) :
        r1, c1 = points[route[0] - 1]
        time_checker[idx].append((r1, c1))
        for i, point in enumerate(route):
            if i >= 1 : 
                r2, c2 = points[point-1]
                r1, c1 = points[route[i-1]-1]
                
                if r2 > r1:
                    for j in range(r1 + 1, r2 + 1):
                        time_checker[idx].append((j, c1))
                elif r2 < r1:
                    for j in range(r1 - 1, r2 - 1, -1):
                        time_checker[idx].append((j, c1))

                if c2 > c1:
                    for j in range(c1 + 1, c2 + 1):
                        time_checker[idx].append((r2, j))
                elif c2 < c1:
                    for j in range(c1 - 1, c2 - 1, -1):
                        time_checker[idx].append((r2, j))
                        
    max_len = max([len(path) for path in time_checker])
    answer = 0

    for j in range(max_len):            
        check_dict = dict()
        for idx, path in enumerate(time_checker):
            if j < len(path):
                pos = path[j]
                if pos in check_dict:
                    check_dict[pos] += 1
                    if check_dict[pos] == 2:
                        answer += 1
                else:
                    check_dict[pos] = 1

    return answer
                    
                               
    return answer