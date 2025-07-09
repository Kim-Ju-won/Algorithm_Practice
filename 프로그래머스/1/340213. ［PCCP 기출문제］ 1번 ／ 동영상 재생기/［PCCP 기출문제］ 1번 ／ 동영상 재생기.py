def solution(video_len, pos, op_start, op_end, commands):

    
    video_len = list(map(int, video_len.split(":")))
    pos = list(map(int, pos.split(":")))
    op_start = list(map(int, op_start.split(":")))
    op_end = list(map(int, op_end.split(":")))
    
    video_len = video_len[0]*60 + video_len[1]
    pos = pos[0]*60 + pos[1]
    op_start = op_start[0]*60 + op_start[1]
    op_end = op_end[0]*60 + op_end[1]
    
    for command in commands : 
        if command == "next":
            if op_start <= pos < op_end : 
                pos = op_end
            pos = min(video_len, pos+10)
            if op_start <= pos < op_end : 
                pos = op_end
        elif command == "prev":
            if op_start <= pos < op_end : 
                pos = op_end
            pos = max(0, pos - 10)
            if op_start <= pos < op_end : 
                pos = op_end
                
    m = "0"+str(pos//60) if pos//60 < 10 else str(pos//60) 
    s = "0"+str(pos%60) if pos%60 < 10 else str(pos%60)
    return ":".join([m,s])