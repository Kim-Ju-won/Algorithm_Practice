def solution(rank, attendance):
    rank_dict = dict()
    for i, v in enumerate(rank): 
        if attendance[i] == True : 
            rank_dict[v] = i 
    rank_list = sorted(list(rank_dict.keys()))
    return rank_dict[rank_list[0]] * 10000 + rank_dict[rank_list[1]] *100 + rank_dict[rank_list[2]]