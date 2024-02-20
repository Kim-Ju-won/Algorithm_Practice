def solution(my_string, indices):
    for i in indices : 
        my_string = my_string[:i]+'_'+my_string[i+1:]
    return ''.join(my_string.split('_'))