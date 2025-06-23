def solution(n):
    answer = 0
    n_str = str(n)
    arr = []
    for i in n_str:
        arr.append(i)
    arr.sort(reverse=True)
    n_str = ''
    for i in arr:
        n_str += i
    answer = int(n_str)
    return answer