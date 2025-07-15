def solution(dots):
    answer = 0
    
    answer = abs(dots[0][0] - dots[1][0]) * abs(dots[1][1] - dots[2][1])
    
    if dots[0][0] != dots[1][0]:
        answer = abs(dots[0][0] - dots[1][0]) * abs(dots[1][1] - dots[2][1])
    elif dots[1][0] != dots[2][0]:
        answer = abs(dots[1][0] - dots[2][0]) * abs(dots[2][1] - dots[3][1])
    else:
        answer = abs(dots[2][0] - dots[3][0]) * abs(dots[3][1] - dots[0][1])
    return answer