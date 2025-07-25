def solution(s):
    answer = ''
    arr = []
    arr_int = []
    
    arr = s.split(" ")
    
    for i in arr:
        arr_int.append(int(i))
    
    arr_int.sort()
        
    answer = str(arr_int[0]) + " " + str(arr_int[-1])
    
    return answer