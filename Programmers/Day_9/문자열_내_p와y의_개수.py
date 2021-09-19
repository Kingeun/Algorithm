def solution(s):
    y_cnt=0
    p_cnt=0
    s=s.lower()
    
    for i in range(len(s)):
        if s[i]=='y':
            y_cnt+=1
        if s[i]=='p':
            p_cnt+=1
            
    if y_cnt==p_cnt:
        return True
    else:
        return False
    
# 다른 사람 풀이

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
    
