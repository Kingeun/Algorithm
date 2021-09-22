#2869 -> 시간초과
a,b,v=map(int,input().split())
cnt=1  #걸린 날짜
loc=0 #현재 위치

if a>=v:
        print(1)

else :
    while v>loc:
        if loc+a<v:
            loc+=(a-b)
            cnt+=1
            
#        else:
#            break
        
    print(cnt)  
    
    
# 다른 사람풀이->빠르다..
import sys
import math

a,b,v=map(int,input().split())
cnt=((v-a)/(a-b))+1  #cnt=v / (a - b)이면 정상에 올라갔어도 밤에 내려와서 다음 날 다시 올라가는 불상사가 발생
print(math.ceil(cnt))  #올림처리
