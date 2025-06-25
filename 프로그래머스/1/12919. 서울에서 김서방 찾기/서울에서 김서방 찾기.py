def solution(seoul):
    answer = ''
    num = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            num = str(i)
            answer = "김서방은 " + num + "에 있다"
            break
    
    return answer