def solution(letter):
    answer = ''
    arr = []
    
    arr = letter.split(' ')
    
    m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    for i in range(len(arr)):
        answer += chr(m.index(arr[i])+97)
    
    return answer