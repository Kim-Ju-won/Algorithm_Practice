'''
Question : 
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
- phone_book의 길이는 1 이상 1,000,000 이하입니다.
  - 각 전화번호의 길이는 1 이상 20 이하입니다.
  - 같은 전화번호가 중복해서 들어있지 않습니다.
입출력 예제
phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
'''

def solution(phone_book):
    phone_book_len = dict()
    for ele in phone_book : 
        if len(ele) not in phone_book_len : 
            phone_book_len[len(ele)] = {ele:0}
        else : 
            phone_book_len[len(ele)][ele] = 0
            
    for key in phone_book_len :
        for ele in phone_book : 
            if ele[:key] in phone_book_len[key] : 
                phone_book_len[key][ele[:key]] +=1
                if phone_book_len[key][ele[:key]] == 2 : 
                    return False
    
    return True
    
'''
다른 문제 풀이 
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
'''
