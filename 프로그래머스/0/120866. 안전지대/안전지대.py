def solution(board):
    answer = 0
    
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                if 0<=i-1<len(board[0]) and 0<=j-1<len(board[0]) and board[i-1][j-1] != 1:
                    board[i-1][j-1] = 2
                if 0<=i-1<len(board[0]) and board[i-1][j] != 1:
                    board[i-1][j] = 2
                if 0<=i-1<len(board[0]) and 0<=j+1<len(board[0]) and board[i-1][j+1] != 1:
                    board[i-1][j+1] = 2
                if 0<=j-1<len(board[0]) and board[i][j-1] != 1:
                    board[i][j-1] = 2
                if 0<=j+1<len(board[0]) and board[i][j+1] != 1:
                    board[i][j+1] = 2
                if 0<=i+1<len(board[0]) and 0<=j-1<len(board[0]) and board[i+1][j-1] != 1:
                    board[i+1][j-1] = 2
                if 0<=i+1<len(board[0]) and board[i+1][j] != 1:
                    board[i+1][j] = 2
                if 0<=i+1<len(board[0]) and 0<=j+1<len(board[0]) and board[i+1][j+1] != 1:
                    board[i+1][j+1] = 2
    
    for i in range(len(board[0])):
        answer += board[i].count(0)
    
    return answer