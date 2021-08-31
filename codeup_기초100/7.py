#6088
a,d,n=map(int,input().split())
cnt=a
for i in range(0,n-1):
    cnt+=d
print(cnt)

#6089
a,r,n=map(int,input().split())
cnt=a
for i in range(0,n-1):
    cnt=cnt*r
print(cnt)

#6090번
a,m,d,n=map(int,input().split())
cnt=a
for i in range(0,n-1):
    cnt=cnt*m+d
print(cnt)

