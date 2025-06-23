def solution(n):
    answer = 0
    arr = []
    for i in range(1, n+1):
        if n % i == 1:
            arr.append(i)
    answer = min(arr)
    return answer