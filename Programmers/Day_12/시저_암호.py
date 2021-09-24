def solution(s, n):
    answer = []
    
    for i in range(len(s)):
        if s[i]==' ':
            answer.append(' ')
        
        else:
            answer.append(chr(ord(s[i])+n))
            
        
    return "".join(answer)
