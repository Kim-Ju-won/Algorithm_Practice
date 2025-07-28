from fractions import Fraction

def count_events(P, t1, t2):
    n, d = P.numerator, P.denominator
    k_min = (t1 * d + n - 1) // n
    k_max = (t2 * d) // n
    return max(0, k_max - k_min + 1)

def solution(h1, m1, s1, h2, m2, s2):

    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2

    P_sm = Fraction(3600, 59)    
    P_sh = Fraction(43200, 719)  

    cnt = count_events(P_sm, t1, t2) + count_events(P_sh, t1, t2)
    for T in (0, 43200):
        if t1 <= T <= t2:
            cnt -= 1

    return cnt