import math

def count_events(P, t1, t2):
    k_min = math.ceil(t1 / P)
    k_max = math.floor(t2 / P)
    return max(0, k_max - k_min + 1)
    
def solution(h1, m1, s1, h2, m2, s2):
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 + m2*60 + s2

    P_sm = 3600.0 / 59
    P_sh = 43200.0 / 719

    cnt = count_events(P_sm, t1, t2) + count_events(P_sh, t1, t2)
    for T in (0, 43200):
        if t1 <= T <= t2:
            cnt -= 1
    
    return cnt