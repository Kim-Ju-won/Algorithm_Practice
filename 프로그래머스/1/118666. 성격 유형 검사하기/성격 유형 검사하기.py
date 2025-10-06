def solution(survey, choices):
    answer = ""
    personality = {
        'R':0, 
        'T':0,
        "C":0,
        "F":0,
        "J":0,
        "M":0, 
        "A":0, 
        "N":0
    }
    n = len(survey)
    
    for i in range(n):
        query = survey[i]
        choice = choices[i]
        a, b = query[0], query[1]

        if choice <= 3 : 
            personality[a] += (4-choice)
        elif choice >= 4 : 
            personality[b] += (choice-4)

            
    answer += "R" if personality["R"] >= personality["T"] else "T"
    answer += "C" if personality["C"] >= personality["F"] else "F"
    answer += "J" if personality["J"] >= personality["M"] else "M"
    answer += "A" if personality["A"] >= personality["N"] else "N"

    return answer