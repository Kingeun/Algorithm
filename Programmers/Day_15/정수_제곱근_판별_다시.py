## 내풀이->틀림
import math
def solution(n):
    #print(math.sqrt(n))
    num=isinstance(int(math.sqrt(n)),int)
    
    #print(num)
    
    if num==True:
        answer=(math.sqrt(n)+1)**2
        
    else:
        answer=-1
    return answer

##다른사람풀이->
def solution(n):
    answer = 0
    x = n ** 0.5
    
    if num == int(num):
        answer = (num + 1) ** 2
    else:
        answer = -1
        
    return answer
