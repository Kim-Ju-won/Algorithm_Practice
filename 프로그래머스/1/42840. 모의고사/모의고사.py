def solution(answers):
    answer = []
    arr = [
        [1, 2, 3, 4, 5],
        [1, 3, 4, 5],
        [3, 1, 2, 4, 5],
    ]
    cor = [0, 0, 0]

    for i, v in enumerate(answers):
        for j in range(3):
            if j == 0:
                if arr[j][i % 5] == v:
                    cor[j] += 1
            elif j == 1:
                if i % 2:
                    if arr[j][((i + 1) // 2) % 4 - 1] == v:
                        cor[j] += 1
                else:
                    if v == 2:
                        cor[j] += 1
            if j == 2:
                if arr[j][(i // 2) % 5] == v:
                    cor[j] += 1
    for i in range(3):
        if cor[i] == max(cor):
            answer.append(i + 1)
    return answer