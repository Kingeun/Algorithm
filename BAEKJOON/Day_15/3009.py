#3009

sq_x=[]
sq_y=[]
for i in range(3):
    x,y=map(int,input().split())
    sq_x.append(x)
    sq_y.append(y)

for i in sq_x:
    if sq_x.count(i)==1:
        x_=i
for j in sq_y:
    if sq_y.count(j)==1:
        y_=j
        
print(x_,y_)
