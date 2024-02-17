def solution(strArr):
    return [ele.upper() if i%2 else ele.lower() for i, ele in enumerate(strArr)]