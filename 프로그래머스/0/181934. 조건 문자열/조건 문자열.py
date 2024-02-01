def solution(ineq, eq, n, m):
    metric = ''
    if n > m : 
        metric =['>!', '>=']
    elif n == m : 
        metric = ['<=','>=']
    elif n < m : 
        metric =['<!', '<=']

    return 1 if (ineq+eq) in metric else 0