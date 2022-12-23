import sys

# king queen rook bishop knight pawn
chess_list = list(map(int, sys.stdin.readline().split()))
check_list = [1,1,2,2,2,8]

for i in range(len(chess_list)):
    print(check_list[i]-chess_list[i], end = ' ')