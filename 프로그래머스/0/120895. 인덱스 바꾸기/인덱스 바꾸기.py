def solution(my_string, num1, num2):
    answer = ''
    temp = 0
    
    if num1 > num2:
        tmep = num1
        num1 = num2
        num2 = temp
    
    answer = my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]
    
    return answer