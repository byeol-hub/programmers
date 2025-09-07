def solution(n, times):
    answer = 0
    times.sort()
    start = times[0] # 검사하는데 걸리는 최소 시간
    end = times[-1]*n # 검사하는데 걸리는 최대 시간
    
    while start <= end:
        mid = (start+end)//2
        people = 0 # 현재의 mid 값으로 심사 받을 수 있는 사람의 수
        for i in times:
            people += mid//i
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            end = mid - 1
            
        else:
            start = mid + 1
            
    return answer