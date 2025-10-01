def solution(today, terms, privacies):
    answer = []
    
    for idx, i in enumerate(privacies, start=1):
        for j in terms:
            if i[-1] == j[0]:
                y = int(i[0:4])
                m = int(i[5:7]) + int(j[2:])
                d = int(i[8:10])

                while m > 12:
                    y += 1
                    m -= 12

                d -= 1
                if d == 0:
                    m -= 1
                    if m == 0:
                        m = 12
                        y -= 1
                    d = 28

                if (y < int(today[0:4])) or (y == int(today[0:4]) and m < int(today[5:7])) or (y == int(today[0:4]) and m == int(today[5:7]) and d < int(today[8:10])):
                    answer.append(idx)
    
    return answer
