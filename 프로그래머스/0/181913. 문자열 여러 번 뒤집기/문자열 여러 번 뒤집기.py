def solution(my_string, queries):
    answer = ''
    arr = []
    a = []
    for i in my_string:
        arr.append(i)
    for query in queries:
        a = arr[query[0]:query[1]+1]
        a.reverse()
        i = 0
        for re in a:
            arr[query[0]+i] = re
            i += 1
    for b in arr:
        answer += b
    return answer