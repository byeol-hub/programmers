def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] >= 50:
            arr[i] = arr[i] / 2
        elif arr[i] % 2 == 1 and arr[i] < 50:
            arr[i] = arr[i]*2
    answer = arr
    return answer