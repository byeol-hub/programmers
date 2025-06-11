def solution(strArr):
    answer = 0
    a = []
    for i in strArr:
        a.append(len(i))
    a = set(a)
    a = list(a)
    b = [i for i in range(len(a))]
    for i in range(len(a)):
        b[i] = 0
        for j in strArr:
            if len(j) == a[i]:
                b[i] += 1
    answer = max(b)
    return answer