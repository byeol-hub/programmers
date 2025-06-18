def solution(myStr):
    answer = []
    arr = []
    array = []
    arr = myStr.split("a")
    for i in arr:
        b = i.split("b")
        for j in b:
            c = j.split("c")
            array.append(c)
    for i in array:
        for j in i:
            if j != "":
                answer.append(j)
    if answer == []:
        answer.append("EMPTY")
    return answer