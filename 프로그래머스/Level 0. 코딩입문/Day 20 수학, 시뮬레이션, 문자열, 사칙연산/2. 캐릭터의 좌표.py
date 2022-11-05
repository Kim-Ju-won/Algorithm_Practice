'''
Question : 머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
'''

def solution(keyinput, board):
    keyboard = {
        "left":[-1,0],
        "right":[1,0], 
        "up":[0, 1],
        "down":[0, -1]
    }
    
    answer = [0,0]
    
    width = ((board[0]-1)//2)
    length = ((board[1]-1)//2)
    
    for key in keyinput : 
        move = keyboard[key]
        if key == 'right' and answer[0] < width:
            answer[0] += move[0]
        elif key == 'left' and answer[0] > -width:
            answer[0] += move[0]
        
        if key == 'down' and -length < answer[1]: 
            answer[1] += move[1]
        elif key == 'up' and answer[1] < length:
            answer[1] += move[1]
        
    return answer