![image.png](attachment:image.png)
![image-2.png](attachment:image-2.png)

def gr(n,k):
    cnt = 0
    while True:        
        if n%k==0:
            n/=k
            cnt+=1
        else :
            n-=1
            cnt+=1
        
        if n==1:
            break      
            
    return cnt


n=int(input())
k=int(input())
print(gr(n,k))
