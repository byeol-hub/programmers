def solution(arr):
    answer = 0
    a = []
    while (a != arr):
        a = arr.copy()
        answer += 1
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] = arr[i] / 2
            elif arr[i] % 2 == 1 and arr[i] < 50:
                arr[i] = arr[i]*2+1
    answer -= 1
    return answer