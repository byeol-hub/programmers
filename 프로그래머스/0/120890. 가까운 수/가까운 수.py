def solution(array, n):
    answer = 0
    m = []
    
    array.sort()
    
    for i in array:
        m.append(abs(n-i))
        
    m_min = m.index(min(m))

    answer = array[m_min]
    
    return answer