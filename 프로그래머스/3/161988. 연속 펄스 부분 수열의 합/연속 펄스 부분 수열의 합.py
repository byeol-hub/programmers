def solution(sequence):
    a = 1
    
    '''
    전체 시퀀스 길이만큼의 누적합을 계속 구하면서 배열에 저장하고 최대값-최소값 하기
    '''
    
    # 전체 누적합을 사용하는 경우, 누적합을 사용하지 않는 경우까지 포함
    p = [0]*(len(sequence)+1)
    
    # 1로 시작하는 펄스와 -1로 시작하는 펄스의 결과값은 부호만 다름
    for i in range(len(sequence)):
        p[i+1] = p[i] + sequence[i]*a
        a *= -1
    
    return max(p) - min(p)