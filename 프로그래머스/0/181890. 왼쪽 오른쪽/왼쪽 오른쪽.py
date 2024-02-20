import sys
MAXSIZE = sys.maxsize
def solution(str_list):
    l, r = MAXSIZE, MAXSIZE
    if 'l' in str_list:
        l = str_list.index('l')
    if 'r' in str_list :
        r = str_list.index('r')
    
    if l == MAXSIZE and r == MAXSIZE : 
        return []
    elif l < r : 
        return str_list[:l]
    elif r < l :
        return str_list[r+1:]
    