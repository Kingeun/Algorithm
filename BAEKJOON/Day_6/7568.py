#7568
n=int(input())
body=[]


for i in range(n):
    x,y=map(int,input().split())
    body.append([x,y])

for i in range(n):
    rank=1
    for j in range(n):
        if i!=j:
            if (body[i][0]<body[j][0]) and (body[i][1]<body[j][1]):
                rank += 1
    print(rank,end=' ')
