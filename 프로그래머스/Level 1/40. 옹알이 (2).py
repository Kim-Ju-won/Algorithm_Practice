'''
Question : 
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

제한사항
- 1 ≤ babbling의 길이 ≤ 100
- 1 ≤ babbling[i]의 길이 ≤ 30
- 문자열은 알파벳 소문자로만 이루어져 있습니다.
'''

def solution(babbling):
    answer = 0
    can_speak = ["aya","ye","woo","ma"]
    
    for s in babbling :
        check = True
        for i in range(len(can_speak)) : 
            s=s.replace(can_speak[i], str(i))
        for i in range(len(s)) :
            if '0'> s[i] or s[i] >'3':
                check=False
                break 
            if i >= 1 and s[i]==s[i-1]:
                check=False
                break 
        if check==True :
            answer+=1
    
    return answer

'''
다른 풀이 : 
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
'''