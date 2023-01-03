def solution(numbers):
    answer = []
    count = 0
    for num in numbers: 
        if num == 0: 
            count+=1
        answer.append(str(num))
    if count == len(numbers):
        return '0'
    answer.sort(
        key=lambda x : 4*x,
        reverse=True)
   
    return  ''.join(answer)
'''
    answer = []
    for num in numbers: 
        answer.append(str(num))
    answer.sort(
        key=lambda x : (x,-len(x)) if len(x) >= 3 else (
            (x+x[0],-len(x)) if len(x) == 2 else (x*3,-len(x))),
        reverse=True)
    ans = ''
    i = 0
    while i < len(answer):
        if i+1 < len(answer):
            if answer[i]+answer[i][0] == answer[i+1]:
                if answer[i]+answer[i+1] > answer[i+1]+answer[i]:
                    ans += (answer[i]+answer[i+1])
                else : 
                    ans += (answer[i+1]+answer[i])
                i+=1
            else : 
                ans+=answer[i]
        else : 
            ans+=answer[i]
        i+=1

    return ans
'''
