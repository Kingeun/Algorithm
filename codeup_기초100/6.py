#6080번
n,m=map(int,input().split())

for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)
        
        
#6082
n=int(input())
for i in range(1,n+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9 :
        print('X',end=' ')
    else:
        print(i,end=' ')
        
        
#6083

r,g,b=map(int,input().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
print(r*g*b)


#6084
h,b,c,s=map(int,input().split())
sound=(h*b*c*s)/8/1024/1024
print(format(sound,'.1f'),"MB")


#6085
w,h,b=map(int,input().split())
image=(w*h*b)/8/1024/1024
print(format(image,'.2f'),'MB')


#6086
n=int(input())
cnt=0
i=0
while True:
    cnt+=i
    i+=1
    if cnt>=n:
        break
print(cnt)


#6087
n=int(input())
for i in range(n+1):   
    if i%3 == 0:
        continue
    print(i,end=' ')
    
