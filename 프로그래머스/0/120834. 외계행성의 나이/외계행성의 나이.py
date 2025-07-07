def solution(age):
    answer = ''
    # a: 97
    
    for i in str(age):
        answer += chr(int(i)+97)
    
    return answer