from collections import deque

def solution(queue1, queue2):
    
    answer = 3000001
    queue1_ = deque([ x for x in queue1 ])
    queue2_ = deque([ x for x in queue2 ])
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    maximum_count = len(queue1)
    checking = False
    count = 0 
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    
    if sum_queue1 != sum_queue2 : 
        
        move = queue1.popleft()
        queue2.append(move)
        sum_queue1 -= move
        sum_queue2 += move
        count += 1
        
        while count <= maximum_count*3 and queue1 and queue2 :
            
            if sum_queue1 < sum_queue2 : 
                move = queue2.popleft()
                queue1.append(move)
                sum_queue1 += move
                sum_queue2 -= move
                count += 1
    
            elif sum_queue1 > sum_queue2 : 
                move = queue1.popleft()
                queue2.append(move)
                sum_queue1 -= move
                sum_queue2 += move
                count += 1
                
            else : 
                checking = True 
                answer = count 
                break

        sum_queue1 = sum(queue1_)
        sum_queue2 = sum(queue2_)
        move = queue2_.popleft()
        queue1_.append(move)
        sum_queue1 += move
        sum_queue2 -= move
        count = 1
        
        while count <= maximum_count*3 and queue1_ and queue2_ :
            if sum_queue1 < sum_queue2 : 
                move = queue2_.popleft()
                queue1_.append(move)
                sum_queue1 += move
                sum_queue2 -= move
                count += 1
    
            elif sum_queue1 > sum_queue2 : 
                move = queue1_.popleft()
                queue2_.append(move)
                sum_queue1 -= move
                sum_queue2 += move
                count += 1
                
            else : 
                checking = True 
                answer = min(answer, count)
                break
    else : 
        checking = True
        answer = 0 
        
    return answer if checking else -1