def solution(s):
    count = 0
    count_0 = 0
    
    while s != "1":
        count += 1
        count_0 += s.count("0")
        s = str(int(s.replace("0", "")))
        s = bin(len(s))[2:]
    
    answer = [count, count_0]
    
    return answer