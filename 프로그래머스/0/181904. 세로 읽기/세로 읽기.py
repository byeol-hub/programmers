def solution(my_string, m, c):
    answer = ''
    a = ''
    for i in range(m, len(my_string)+1, m):
        a = my_string[i-m:i]
        answer += a[c-1]
    return answer