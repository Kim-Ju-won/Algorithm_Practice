def solution(genres, plays):
    genre_order = dict()
    num_order = dict()
    record_play = dict()
    answer =[]
    for i in range(len(genres)):
        if genres[i] in genre_order : 
            genre_order[genres[i]] += plays[i]
        else : 
            genre_order[genres[i]] = plays[i]

        if genres[i] in record_play : 
            record_play[genres[i]].append([plays[i],i])
        else : 
            record_play[genres[i]]= [[plays[i],i]]
    for key in genre_order : 
        num_order[genre_order[key]] = key
    
    keys = list(num_order.keys())
    keys.sort(reverse=True)
    
    for key in keys : 
        gen = num_order[key] 
        record_play[gen].sort(reverse=True, key=lambda x : (x[0],-x[1]))
        for i in range(len(record_play[gen])):
            if i < 2:
                answer.append(record_play[gen][i][1])
    
    return answer