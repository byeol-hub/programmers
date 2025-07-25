def solution(l, r):
    ans = []
    answer = []
    array = ["0", "5"]
    count = 0
    
    for i in range(l,r+1):
        if (i % 5 == 0):
            count = 0
            for j in str(i):
                if j in array:
                    count += 1
                    continue
                else:
                    break
            if count == len(str(i)):
                answer.append(str(i).replace('5','1'))
                break
                
    for i in range(r, l-1, -1):
        if (i % 5 == 0):
            count = 0
            for j in str(i):
                if j in array:
                    count += 1
                    continue
                else:
                    break
            if count == len(str(i)):                
                answer.append(str(i).replace('5','1'))
                break
                
    if answer != []:
        for i in range(int(answer[0], 2), int(answer[1], 2) + 1):
            ans.append(int(((bin(i))[2:]).replace('1','5')))
    else:
        ans.append(-1)
    
    return ans