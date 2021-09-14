## 1
def solution(n,lost,reserve):
    student=[1]*n  #모든 학생들이 체육복을 가지고 있음
    # [1 1 1 ... 1]
    
    #집합으로 바꾸기
    lost=set(lost) 
    reserve=set(reserve)
    
    #교집합으로 빼주기
    inter=lost.intersection(reserve)
    
    lost=lost-inter
    reserve=reserve-inter
    
    #print(lost)
    #print(reserve)
    
    for i in lost:
        student[i-1]=0
    
    
    for j in reserve:
        if j==1:  #1번학생
            if student[j]==0:
                student[j]=1
            
        elif j==len(student):  #마지막 학생
            if student[j-2]==0:  #마지막 바로 앞의 학생
                student[j-2]=1
                
        else: #사이의 값들
            if student[j-2]==0:
                student[j-2]=1
            elif student[j]==0:
                student[j]=1
            else:
                continue
            
    answer=0
    for a in student:
        if a==1:
            answer+=1
            
    #print(student)
    return answer


## 2
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

##https://programmers.co.kr/learn/courses/30/lessons/42862
