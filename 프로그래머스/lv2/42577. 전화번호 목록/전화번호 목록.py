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
