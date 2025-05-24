def solution(num_list):
    answer = 0
    x = 1
    s = 0
    for i in num_list:
        x *= i
        s += i
    s *= s
    print(x, s)
    if x <= s:
        answer = 1
    return answer
