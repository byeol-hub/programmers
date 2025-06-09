def solution(binomial):
    answer = 0
    for i in range(len(binomial)):
        if binomial[i] == "+":
            answer = int(binomial[:i-1]) + int(binomial[i+2:])
        elif binomial[i] == "-":
            answer = int(binomial[:i-1]) - int(binomial[i+2:])
        elif binomial[i] == "*":
            answer = int(binomial[:i-1]) * int(binomial[i+2:])
    return answer