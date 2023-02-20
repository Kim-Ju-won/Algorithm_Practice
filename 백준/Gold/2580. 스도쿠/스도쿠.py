import sys
sys.setrecursionlimit(10**5)

def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end = ' ')
        print()

def sudoku_backtrack(sudoku, check_list, index):
    global check 
    if check == False : 
        if index == len(check_list): 
            print_sudoku(sudoku)
            check = True
            return 
        else : 
            i, j = check_list[index]
            one_nine = set(range(1,10))
            for k in range(9):
                if sudoku[i][k] in one_nine : 
                    one_nine.remove(sudoku[i][k])
            if len(one_nine) >= 1 : 
                for k in range(9):
                    if sudoku[k][j] in one_nine : 
                        one_nine.remove(sudoku[k][j])
            row = i//3
            col = j//3
            if len(one_nine) >= 1 : 
                for m in range(row*3, row*3+3):
                    for n in range(col*3, col*3+3):
                        if sudoku[m][n] in one_nine : 
                            one_nine.remove(sudoku[m][n])
            answers = list(one_nine)
            if len(answers) >= 1 : 
                for ans in answers: 
                    sudoku[i][j] = ans
                    sudoku_backtrack(sudoku,check_list, index+1)
                    sudoku[i][j] = 0
                    
sudoku = [ list(map(int, sys.stdin.readline().split())) for _ in range(9)]
check = False

check_list = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0 : 
            check_list.append((i,j))

sudoku_backtrack(sudoku, check_list,0)



