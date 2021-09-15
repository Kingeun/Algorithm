#1978->참고
## 소수
# 1보다 큰 자연수 중 1과 자기자신만을 약수로 가지는 수로 정의

def prime(n):
    so=0
      
    for i in range(1,n):  #자기자신은 나눠주지 않는다
        if n%i==0:
            so+=1
            
    if so==1:
        return True  #1을 반환
    
    else :
        return False #0을 반환
            
        
n=int(input())
b=list(map(int,input()))
cnt=0

for i in b:
    so+=prime(i)  ##함수에 하나씩 넣는다.
    
print(cnt)  ##소수의 개수
