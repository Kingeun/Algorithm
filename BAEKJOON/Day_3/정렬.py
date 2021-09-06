#2108
n=int(input())
a=[]

for i in range(n):
    a.append(int(input()))

#1
su=0
for i in a:
    su+=i
mean=su/n

#2
b=sorted(a)
median=b[int(((len(b)+1)/2)-1)]
    
#3 ??모르겠다 

cnt=[]
for i in range(len(b)):
    
    

#4
ran=max(a)-min(a)
    
print(mean)
print(round(median,1))
print(mode)
print(ran)


#11650
n=int(input())
c=[]
for i in range(n):
    x,y=map(int,input().split())
    c.append([x,y])
    
c.sort()

for i in range(n):
    print(c[i][0],c[i][1])
    
    
  #11651
import sys
n=int(sys.stdin.readline())
c=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    c.append([y,x])
    
c.sort()

for i in range(n):
        
    print(c[i][1],c[i][0])  


    
    

