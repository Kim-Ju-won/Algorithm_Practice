def in_range(x,y):
    return True if 1<= x <= 8 and 1 <= y <= 8 else False

direction = {
    "R":[1,0],
    "L":[-1,0],
    "B":[0,-1],
    "T":[0,1],
    "RT":[1,1],
    "LT":[-1,1],
    "RB":[1,-1],
    "LB":[-1,-1]
}

formatting_chess = {
    'A':1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8
}

convert_chess = {
    1:'A',
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H"
}

chess = [[0 for _ in range(8)] for _ in range(8)]

king, dol, n = tuple(input().split())
n = int(n)
moves = [ input().rstrip() for _ in range(n)]

r, c = formatting_chess[king[0]], int(king[1])
r2, c2 = formatting_chess[dol[0]], int(dol[1])

for move in moves :
    x, y =direction[move]
    if in_range(r+x,c+y):
        if r+x == r2 and c+y == c2 :
            if in_range(r2+x, c2+y) : 
                r, c = r+x, c+y
                r2, c2 = r2+x, c2+y 
        else : 
            r, c = r+x, c+y

print(f"{convert_chess[r]}{c}")
print(f"{convert_chess[r2]}{c2}")