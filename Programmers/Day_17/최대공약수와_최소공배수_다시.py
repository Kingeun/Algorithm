def solution(n, m): -> 다시
    answer = []
    max_=[]
    min_=[]
    
    for i in range(1,min(n,m)):
        if n%i==0 and m%i==0:
            max_.append(i)
        
    if len(max_) != 1:
        max_.remove(1)
        answer.append(min(max_))            
    else :
        answer.append(min(max_))
    
    for j in range(1,max(n,m)):
        if n%j==0 or m%j==0:
            min_.append(j)
    answer.append(max(min_))
    
    return answer
