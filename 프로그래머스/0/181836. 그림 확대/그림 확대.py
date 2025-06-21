def solution(picture, k):
    answer = []
    a = ''
    for i in picture:
        for j in range(k):
            for x in i:
                a += x*k
            answer.append(a)
            a = ''
    return answer