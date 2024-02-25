def solution(picture, k):
    answer = []
    for pixel in picture : 
        pixel = pixel.replace('x', 'x'*k)
        pixel = pixel.replace('.', '.'*k)
        for _ in range(k):
            answer.append(pixel)
    return answer