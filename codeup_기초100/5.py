#6077
n=int(input())
cnt=0
for i in range(1,n+1):
    if i%2==0:
        cnt+=i
print(cnt)


#6078

while True:
    n=input()
    print(n)
    if n=='q':
        break
        
#6079
n=int(input())
cnt=0

for i in range(1,n):
    
    if cnt<n:
        cnt+=i
        #print(i)
    else:
        break

print(i-1)      
 
