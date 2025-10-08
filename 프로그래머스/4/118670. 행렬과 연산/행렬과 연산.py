from collections import deque

def solution(rc, operations):
    R, C = len(rc), len(rc[0])

    left = deque([row[0] for row in rc])                # 첫 열
    right = deque([row[-1] for row in rc])              # 마지막 열
    mid = deque([deque(row[1:-1]) for row in rc])       # 중간 부분

    for op in operations:
        if op == "ShiftRow":
            left.rotate(1)
            right.rotate(1)
            mid.rotate(1)

        elif op == "Rotate":
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[-1].append(right.pop())
            left.append(mid[-1].popleft())

    answer = []
    for i in range(R):
        answer.append([left[i]] + list(mid[i]) + [right[i]])
    return answer