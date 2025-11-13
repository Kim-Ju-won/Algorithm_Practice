import sys

s = sys.stdin.readline().rstrip()

word_list = []
tag_list = []
tag_checker = False 
tag = ""
word = ""
count = 0 

for i in range(len(s)):
    if s[i] == "<":
        word_list.append([word, count])
        word = ""
        count += 1
        tag += s[i]
        tag_checker = True
        
    elif s[i] == ">" :
        tag += s[i]
        tag_list.append([tag, count])
        tag = ""
        count += 1
        tag_checker = False 
    else : 
        if tag_checker : 
            tag += s[i]
        else : 
            if s[i] == " ":
                word_list.append([word, count])
                word = ""
                count += 1
            else : 
                word += s[i]

if word != "" : 
    word_list.append([word, count])

for i in range(len(word_list)) : 
    word_list[i][0] = word_list[i][0][::-1]

answer_dict = dict()
for i in range(count) :
    answer_dict[i] = ""
    
for word in word_list : 
    w, idx = word 
    answer_dict[idx] = ["word",w]
    
for tag in tag_list : 
    t, idx = tag
    answer_dict[idx] = ["tag",t]

answer = answer_dict[0][1]
for key, value in answer_dict.items():
    if key != 0:
        if  answer_dict[key][0] == "tag":
            answer += value[1]
        elif answer_dict[key][0] == "word":
            if answer_dict[key-1][0] == "word":
                answer += " "
            answer += value[1]
print(answer)