def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    a = pat.lower()
    if a in myString:
        answer = 1
    return answer