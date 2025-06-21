def solution(arr):
    answer = [[]]
    count = 0
    a = []
    for i in arr:
        count = len(i)
        break
    if len(arr) > count:
        for i in arr:
            for j in range((len(arr) - count)):
                i.append(0)
            answer.append(i)
    elif len(arr) < count:
        for i in range(count):
            a.append(0)
        for i in range(count - len(arr)):
            arr.append(a)
        answer = arr
    else:
        answer = arr
    if [] in answer:
        answer.remove([])
    return answer