def solution(s):
    s=s.split(' ')
    #print(s)
    #print(s[0])
    answer=[]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2==0:
                answer.append(s[i][j].upper())
            else:
                answer.append(s[i][j].lower())
        answer.append(' ')
    
    return ''.join(answer[:-1])
  
  
## https://programmers.co.kr/learn/courses/30/lessons/12930
