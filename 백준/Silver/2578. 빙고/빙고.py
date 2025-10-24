bingo = [ list(map(int, input().split())) for _ in range(5)]
speak = [ list(map(int, input().split())) for _ in range(5)]
speak = speak[0] + speak[1] + speak[2] + speak[3] + speak[4]

def in_range(x,y):
    return True if 0 <= x < 5 and 0 <= y < 5 else False 

bingo_checker = [([-1,0],[1,0]), ([0,-1],[0,1]), ([1,1],[-1,-1]), ([1,-1],[-1,1])]
iter_count = 0 
total_bingo = 0 
bingo_list = []
for idx, number in enumerate(speak) :
    
    checker = set()
    for i in range(5):
        for j in range(5) : 
            if bingo[i][j] == number : 
                bingo[i][j]="X"
                checker=(i,j)
                break
        if checker : 
            break 
    temp = set()
    if checker: 
        r, c = checker
        
        for checking in bingo_checker : 
            temp =set([(r,c)])
            start, end = checking
            bingo_count = 1    
            k = 1
            x,y = start 

            while in_range(r+k*x, c+k*y): 
                if bingo[r+k*x][c+k*y] == "X":
                    bingo_count += 1
                    temp.add((r+k*x,c+k*y))

                else : 
                    break 
                k += 1
            
            k = 1
            x,y = end

            while in_range(r+k*x, c+k*y): 
                if bingo[r+k*x][c+k*y] == "X":
                    bingo_count += 1
                    temp.add((r+k*x,c+k*y))
                else : 
                    break 
                k += 1

            if bingo_count == 5 :
                countable = True
                for b_list in bingo_list : 
                    if temp == b_list : 
                        countable = False 
                        break 
                    
                if countable:
                    total_bingo += 1 
                    bingo_list.append(temp)

            if total_bingo == 3 : 
                iter_count = idx + 1

                break 

    if total_bingo == 3 : 
        break 

print(iter_count)

    
        
        

    