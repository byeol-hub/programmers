def solution(x):
    answer = True
    x_str = str(x)
    sum = 0
    for i in x_str:
        sum += int(i)
    if x % sum != 0:
        answer = False
    return answer