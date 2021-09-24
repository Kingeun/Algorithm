##4948 -> 실패

def prime(n):
    so=0
        
    for i in range(1,n):
        if n%i==0:
            so+=1
                
    if so==1:
        return True
    else:
        return False
        

while True:            
    n=int(input())
    if n==0:
        break
        
    else:
        num=range(n,2*n+1)

        for i in num:
            cnt+=prime(i)  
            print(cnt)
