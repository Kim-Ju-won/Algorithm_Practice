def findout_formation(x, op, y, z, candidate):
    new_candidate = set()

    for c in candidate : 
        new_x = 0 
        for i in range(len(x)):
            new_x += (int(x[i]))*(c**(len(x)-1-i))
        
        new_y = 0 
        for i in range(len(y)):
            new_y += (int(y[i]))*(c**(len(y)-1-i))
        
        new_z = 0 
        for i in range(len(z)):
            new_z += (int(z[i]))*(c**(len(z)-1-i))
        if op == "+":
            if new_x+new_y == new_z :
                new_candidate.add(c)      
        
        else : 
            if new_x-new_y == new_z :
                new_candidate.add(c) 
    
    return new_candidate

def restore(x, op, y, z, candidate):
    answer = set()
    for c in candidate : 
        new_x = 0 
        if x != "X": 
            for i in range(len(x)):
                new_x += (int(x[i]))*(c**(len(x)-1-i))
        
        new_y = 0 
        if y != "X":
            for i in range(len(y)):
                new_y += (int(y[i]))*(c**(len(y)-1-i))
        
        new_z = 0 
        if z != "X":
            for i in range(len(z)):
                new_z += (int(z[i]))*(c**(len(z)-1-i))
        if op == "+":
            if z == "X" :
                new_z = new_x + new_y
                check_z = ""
                if new_z == 0:
                    check_z = "0"
                while new_z : 
                    check_z += str(new_z % c)
                    new_z //= c 
                answer.add(check_z[::-1])
            elif y == "X": 
                new_y = new_z -new_x 
                check_y = ""
                if new_y == 0:
                    check_y = "0"
                while new_y : 
                    check_y += str(new_y % c)
                    new_y //= c
                answer.add(check_y[::-1])
            elif x == "X": 
                new_x = new_z -new_y 
                check_x = ""
                if new_x == 0:
                    check_x = "0"
                while new_x : 
                    check_x += str(new_x % c)
                    new_x //= c
                answer.add(check_x[::-1])
            
        else : 
            if z == "X" :
                new_z = new_x - new_y
                check_z = ""
                if new_z == 0:
                    check_z = "0"
                while new_z : 
                    check_z += str(new_z % c)
                    new_z //= c 
                answer.add(check_z[::-1])
            elif y == "X": 
                new_y = new_z - new_x
                new_y = 0 - new_y
                check_y = ""
                if new_y == 0:
                    check_y = "0"
                while new_y : 
                    check_y += str(new_y % c)
                    new_y //= c
                answer.add(check_y[::-1])
            elif x == "X": 
                new_x = new_z + new_y 
                check_x = ""
                if new_x == 0:
                    check_x = "0"
                while new_x : 
                    check_x += str(new_x % c)
                    new_x //= c
                answer.add(check_x[::-1])
                
    if len(answer) == 1 :
        if x == "X":
            x = list(answer)[0]
        elif y == "X":
            y = list(answer)[0]
        elif z == "X":
            z = list(answer)[0]
        
        if op == "+" : 
            return f"{x} + {y} = {z}"
        elif op == "-": 
            return f"{x} - {y} = {z}"
    else : 
        if x == "X":
            x = "?"
        elif y == "X":
            y = "?"
        elif z == "X":
            z = "?"
        
        if op == "+" : 
            return f"{x} + {y} = {z}"
        elif op == "-": 
            return f"{x} - {y} = {z}"
    

def solution(expressions): 
    hints = {
        "+":[],
        "-":[]
    }
    find_answer = []
    max_k = 0 
    
    for expression in expressions : 
        expression = expression.split()
        equation = []
        checker = False
        
        for i in range(0, 5, 2):
            equation.append(expression[i])
            if expression[i] == "X":
                checker = True
            else : 
                for check_max in expression[i] : 
                    max_k = max(int(check_max), max_k)
        
        if expression[1] == "+":
            if checker : 
                find_answer.append(equation+["+"])
            else : 
                hints["+"].append(equation)
        else : 
            if checker : 
                find_answer.append(equation+["-"])
            else : 
                hints["-"].append(equation)
                
    candidate = set([i for i in range(max_k+1,10)])
    for op, items in hints.items():
        for item in items : 
            x, y, z = item
            candidate =  findout_formation(x, op, y, z, candidate)
    answer = []
    
    for items in find_answer:
        x, y, z, op = items 
        answer.append(restore(x, op, y, z, candidate))
    
    return answer