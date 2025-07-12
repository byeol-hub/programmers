def solution(numbers):
    answer = ''
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ''
    
    for i in range(len(numbers)):
        num += numbers[i]
        if num in num_list:
            for j in range(len(num_list)):
                if num == num_list[j]:
                    answer += str(j)
                    num = ''
                    break
                    
    answer = int(answer)
    
    return answer