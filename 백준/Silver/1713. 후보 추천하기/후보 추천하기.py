import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
recommend_list = list(map(int, sys.stdin.readline().split()))
photos = []
set_photos = set()

for recommend in recommend_list : 
    for i in range(len(photos)):
        photos[i][2] += 1
    if recommend in set_photos : 
        idx = 0 
        for i in range(len(photos)): 
            if photos[i][0] == recommend : 
                photos[i][1] += 1

    else : 
        if len(photos) >= n :
            photo = photos[-1][0]  
            photos.pop()
            set_photos.remove(photo)
        photos.append([recommend, 1, 1])
        set_photos.add(recommend)

    photos.sort(key= lambda x: (-x[1], x[2]))

answer = []
for i in range(len(photos)):
    answer.append(photos[i][0])

answer.sort()
for ele in answer : 
    print(ele, end= " ")