def solution(myString, pat):
    answer = ''
    arr = []
    for i in range(len(myString)):
        if myString[i:len(pat)+i] == pat:
            arr = myString[:len(pat)+i]
    for i in arr:
        answer += i
    return answer