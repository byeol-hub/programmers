def solution(arr1, arr2):
    answer = [[]]
    
    answer = arr1.copy()
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer