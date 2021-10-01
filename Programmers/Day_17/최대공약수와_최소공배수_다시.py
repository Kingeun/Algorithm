##다시

def solution(n, m):
    answer = []
    max_=[]
    
    
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            max_.append(i)
        
    if len(max_) != 1:
        max_.remove(1)
        answer.append(min(max_))            
    else :
        answer.append(min(max_))
    
    min_=(n*m)/min(max_)
    answer.append(min_)
    return answer
