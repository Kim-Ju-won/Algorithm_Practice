from collections import deque

def solution(coin, cards):
    
    n = len(cards)
    start = cards[:n//3]
    need = set()
    remain_card = [0 for _ in range(n+1)]
    
    for s in start : 
        remain_card[s] = 1

    cards = cards[n//3:]    
    else_checker = set()
    new_round = 0 

    for i in range(0, len(cards),2):
        new_round+= 1
        checking = False
        c1, c2 = cards[i], cards[i+1]
        else_checker.add(c1)
        else_checker.add(c2)

        for j in range(1, len(remain_card)) :
            if remain_card[j] == 1 and remain_card[n+1-j] == 1: 
                remain_card[j] = 0 
                remain_card[n+1-j] = 0
                checking = True 
                break
        
        if checking is False :
            for j in range(1, len(remain_card)) :
                if remain_card[j] == 1 : 
                    if (n+1-j) in else_checker and coin >= 1: 
                        else_checker.remove(n+1-j)
                        remain_card[j] = 0 
                        coin -= 1
                        checking = True 
                        break
            if checking is False : 
                new_else_checker = list(else_checker)
                for j in range(0, len(new_else_checker)):
                    for k in range(j+1, len(new_else_checker)) :
                        if (new_else_checker[j] +new_else_checker[k] == n+1) and coin >= 2: 
                            else_checker.remove(new_else_checker[j])
                            else_checker.remove(new_else_checker[k])
                            checking = True 
                            coin -= 2
                            break
                    if checking : 
                        break

        if checking is False : 
            break
        if i == len(cards)-2 and checking : 
            new_round += 1

    return new_round