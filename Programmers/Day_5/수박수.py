##1
def solution(n):
    
    answer = '수박'*n
    answer = answer[:n]
    return answer

  
##2
def solution(n):
    answer = ''
    for i in range(n):
        if i%2==0:
            answer+='수'
        else:
            answer+='박'
    return answer
