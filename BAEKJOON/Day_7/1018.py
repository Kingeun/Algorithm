#1018

n,m=map(int,input().split())
chess=[]

for _ in range(n):
    stone=input()
    chess.append(stone)
    
count=[] #체스판을 다시 색칠해야 하는 갯수

for s_col in range(n-8+1):
    for s_row in range(n-8+1):
        error_w #w로 시작하는 체스판과 비교 (wbwbwb)
        error_b #b로 시작하는 체스판과 비교 (bwbwbw)
        
        for r in range(s_row,s_row+8):
            for c in range(s_col,s_col+8):
                if (r+c)%2==0:  # 규칙 (row+column) % 2==0 인 행
                    if chess[r][c] != 'w':
                        error_w += 1
                    if chess[r][c] != 'b :
                        error_b += 1
                else:
                    if chess[r][c] != 'b':
                        error_w += 1
                    if chess[r][c] != 'w':
                        error_b += 1
                        
        count.append(error_w)
        count.append(error_b)
        
print(min(count))
