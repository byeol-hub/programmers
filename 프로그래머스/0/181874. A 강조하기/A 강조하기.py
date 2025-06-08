def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer += 'A'
        elif i in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            answer += i.lower()
        else: 
            answer += i
    return answer