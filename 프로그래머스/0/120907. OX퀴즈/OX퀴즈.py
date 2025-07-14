def solution(quiz):
    answer = []
    arr = []
    
    for i in quiz:
        arr = i.split("=")
        if eval(arr[0]) == int(arr[1]):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer