def solution(bandage, health, attacks):
    # 시간, 초당 회복량, 추가 회복량 
    t, x, y = bandage 
    log = [ 0 for _ in range(attacks[-1][0]+1) ]
    log[0] = health 
    # 공격 당함 
    for attack in attacks : 
        time, value = attack 
        log[time] = -value
    # 에너지 계산 
    checker = 0 
    for i in range(1, attacks[-1][0]+1):
        if log[i] < 0 : 
            checker = 0 
            log[i] = log[i-1] + log[i]
            if log[i] <= 0 : 
                return -1
        else : 
            log[i] = min(log[i-1] + x, health)
            checker+=1

            if checker == t : 
                checker = 0 
                log[i] = min(log[i] + y, health)

    return log[-1]