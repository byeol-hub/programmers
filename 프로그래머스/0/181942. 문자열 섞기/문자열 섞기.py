def solution(str1, str2):
    answer = ''
    temp = len(str1)
    for i in range(temp):
        answer += str1[i] + str2[i]
    return answer