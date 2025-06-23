def solution(n):
    import math
    answer = 0
    answer = math.sqrt(n)
    if answer % 1 == 0.0:
        answer = (answer+1)**2
    else:
        answer = -1
    return answer