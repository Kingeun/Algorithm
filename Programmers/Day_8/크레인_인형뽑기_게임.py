def solution(board, moves):
    answer = 0
    b=[]
    for i in moves:
        for j in range(len(board)): #수정
            if board[j][i-1]==0: #열을 기준으로
                continue
            else:
                b.append(board[j][i-1])
                board[j][i-1]=0
                break
                
        if len(b)>1:            
            for i in range(len(b)-1):

                if b[i]==b[i+1]:
                    del b[i]
                    del b[i]
                    #b.pop()
                    answer+=2
                    #break

    return answer
