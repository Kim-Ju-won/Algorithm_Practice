import sys 

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
op = ['+', '-', '*', '//']
operator_list = []
MIN_SIZE =sys.maxsize 
MAX_SIZE = -sys.maxsize


for i in range(len(operators)):
    for _ in range(operators[i]):
        operator_list.append(op[i])
        
def calculator(idx, result):
    global MAX_SIZE
    global MIN_SIZE
    if len(operator_list) == 0: 
        MAX_SIZE = max(MAX_SIZE, result)
        MIN_SIZE = min(MIN_SIZE, result)
    else : 
        for i in range(len(operator_list)) : 
            op = operator_list.pop(i)
            new_result = 0 
            if op =='+':
                new_result = result +number[idx]
            elif op =='*':
                new_result = result * number[idx]
            elif op == '//':
                if result >=0:
                    new_result = result //number[idx]
                else : 
                    new_result = (-result)//number[idx]
                    new_result = - new_result
            else : 
                new_result = result-number[idx]
            calculator(idx+1, new_result)
            operator_list.insert(i, op)


calculator(1,number[0])
print(MAX_SIZE)
print(MIN_SIZE)