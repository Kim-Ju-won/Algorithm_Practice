def solution(expressions):
    gmax = 0
    for expr in expressions:
        A, op, B, _, C = expr.split()
        for ch in A + B + (C if C != 'X' else ''):
            gmax = max(gmax, int(ch))
    possible = {b for b in range(2, 10) if b > gmax}
    for expr in expressions:
        A, op, B, _, C = expr.split()
        if C != 'X':
            for b in list(possible):
                a = 0
                for ch in A:
                    a = a * b + int(ch)
                bb = 0
                for ch in B:
                    bb = bb * b + int(ch)
                c = 0
                for ch in C:
                    c = c * b + int(ch)
                if not ((op == '+' and a + bb == c) or (op == '-' and a - bb == c)):
                    possible.discard(b)
    ans = []
    for expr in expressions:
        A, op, B, _, C = expr.split()
        if C == 'X':
            resset = set()
            for b in possible:
                a = 0
                for ch in A:
                    a = a * b + int(ch)
                bb = 0
                for ch in B:
                    bb = bb * b + int(ch)
                r = a + bb if op == '+' else a - bb
                if r == 0:
                    s = '0'
                else:
                    digs = []
                    while r > 0:
                        digs.append(str(r % b))
                        r //= b
                    s = ''.join(reversed(digs))
                resset.add(s)
            fill = resset.pop() if len(resset) == 1 else '?'
            ans.append(f"{A} {op} {B} = {fill}")
    return ans