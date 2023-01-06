def solution(participant, completion):
    participant_dict = dict()
    for ele in participant : 
        if ele in participant_dict :
            participant_dict[ele] +=1
        else : 
            participant_dict[ele] = 1
    for ele in completion : 
        if ele in participant_dict : 
            participant_dict[ele]-=1

    for key in participant_dict.keys():
        if participant_dict[key] == 1: 
            return key
