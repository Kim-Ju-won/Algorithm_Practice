def solution(friends, gifts):
    answer = 0
    friends_dict = dict()
    friend_number = dict()
    for friend in friends : 
        friends_dict[friend] = dict()
        friend_number[friend] = {"give":0, "receive":0, "number":0}
    for key in friends_dict: 
        for friend in friends: 
            if key != friend : 
                friends_dict[key][friend] = 0 
    
    for gift in gifts : 
        give, get = gift.split()
        friends_dict[give][get] +=1
        friend_number[give]["give"] += 1
        friend_number[get]["receive"] += 1
        
    for key in friend_number : 
        friend_number[key]["number"] = friend_number[key]["give"] - friend_number[key]["receive"]
    
    print(friend_number)
    
    max_num = -1
    
    for key in friends : 
        temp = 0
        for friend in friends_dict[key]:
            if friends_dict[key][friend] > 0 or friends_dict[friend][key] > 0 : 
                if friends_dict[key][friend] != friends_dict[friend][key] :
                    if friends_dict[key][friend] > friends_dict[friend][key] :
                        temp += 1
                else : 
                    if friend_number[key]["number"] > friend_number[friend]["number"]:
                        temp += 1
            else : 
                if friend_number[key]["number"] > friend_number[friend]["number"]:
                    temp += 1
                    
        if temp > max_num : 
            max_num = temp
                        
                    
                        
                        
            
    ##선물 받은 기록이 있다면
    ### 더 많은 선물을 준사람이 받음 +1                           
    ## 받은 경우가 없다면
    ### 선물지수가 더 작은 사람에게 선물 지수가 큰사람이 1개를 받음
    ### 선물지수 = 이번달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수 
    ### 선물지수 같으면 주고 받지도 앖음           
    
    #### 선물을 가장 많이 받을 친구가 받을 선물의 수 
    
    return max_num