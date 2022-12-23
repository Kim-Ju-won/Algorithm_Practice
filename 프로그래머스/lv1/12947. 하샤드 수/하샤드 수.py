def solution(x):
    dnum = 0 
    check = x 
    while check != 0 : 
        dnum += check%10
        check//=10
    if x % dnum == 0 : 
        return True
    else : 
        return False