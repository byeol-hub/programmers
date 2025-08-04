def solution(dots):
    answer = 0
    
    for i in range(1,len(dots)):
        if i == 1:
            if (dots[0][1] - dots[i][1])/(dots[0][0] - dots[i][0]) == (dots[2][1] - dots[3][1])/(dots[2][0] - dots[3][0]):
                answer = 1
                break
        elif i == 2:
            if (dots[0][1] - dots[i][1])/(dots[0][0] - dots[i][0]) == (dots[1][1] - dots[3][1])/(dots[1][0] - dots[3][0]):
                answer = 1
                break
        elif i == 3:
            if (dots[0][1] - dots[i][1])/(dots[0][0] - dots[i][0]) == (dots[1][1] - dots[2][1])/(dots[1][0] - dots[2][0]):
                answer = 1
                break
    
    return answer