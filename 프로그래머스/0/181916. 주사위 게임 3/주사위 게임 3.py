def solution(a, b, c, d):
    abcd = [a,b,c,d]
    if len(set(abcd)) == 4 : 
        return min(a,b,c,d)
    elif len(set(abcd)) == 3 : 
        q_r = []
        for ele in list(set(abcd)):
            count = [a,b,c,d].count(ele)
            if count == 1 : 
                q_r.append(ele)
        return q_r[0]*q_r[1]
    elif len(set(abcd)) == 1 : 
        return a*1111
    else :  
        pq_dict = {}
        for ele in list(set(abcd)):
            count = [a,b,c,d].count(ele)
            pq_dict[ele] = count
            
        if 2 in pq_dict.values():
            p, q = pq_dict.keys()
            return (p + q) * abs(p-q)
        else : 
            p = 0 
            q = 0 
            for k in pq_dict : 
                if pq_dict[k] == 3 : 
                    p = k
                else : 
                    q = k
            return  (10 * p + q)**2
    
    return answer