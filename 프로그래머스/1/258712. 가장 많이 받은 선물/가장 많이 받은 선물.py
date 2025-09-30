def solution(friends, gifts):
    friends_dict = dict()
    friends_checker = dict()
    answer = 0 
    
    for friend in friends : 
        friends_dict[friend] = {
            "recieve":0,
            "sent":0,
            "ratio":0
        }
        friends_checker[friend] = dict()
        for key in friends : 
            friends_checker[friend][key] = 0
    
    for gift in gifts : 
        give, recieve = gift.split()
        
        # 선물지수 
        friends_dict[give]["sent"] += 1
        friends_dict[recieve]["recieve"] += 1
        friends_checker[give][recieve] += 1
        
    for friend in friends : 
        friends_dict[friend]["ratio"] = friends_dict[friend]["sent"] - friends_dict[friend]["recieve"]
        
    max_num = 0 
    for A in friends : 
        A_count = 0 
        for B in friends : 
            if A != B : 
                if friends_checker[A][B] > friends_checker[B][A] :
                    A_count += 1
                    print(B, friends_checker[A][B],friends_checker[B][A] )
                elif friends_checker[A][B] == friends_checker[B][A] : 
                    if friends_dict[A]["ratio"] > friends_dict[B]["ratio"] : 
                        A_count += 1
                        print(B, friends_dict[A]["ratio"], friends_dict[B]["ratio"]  )
        max_num = max(max_num, A_count)
    return max_num