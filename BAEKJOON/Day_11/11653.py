#11653 

def factor(n):
    #prime=[]
    if n==1:
        print('')
    
    for i in range(2,n+1):
        if n%i==0:
            while n%i==0: #i로 나눌 수 없을 때까지 나누기
                #prime.append(i)
                print(i)
                n=n/i
                
    #for j in range(len(prime)):
    #    b=print(prime[j])
    #return b
 

n = int(input())
factor(n)
