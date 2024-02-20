def solution(num_list):
    multiple = 1
    for ele in num_list:
        multiple*=ele
    return 1 if sum(num_list)**2 > multiple else 0