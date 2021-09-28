# 4153번

while True:
    
    tr=list(map(int,input().split()))
    if sum(tr)==0:
        break
        
    else:
        a=[] #짧은변
        b=[] #긴변
        for i in range(len(tr)):

            max_=tr.index(max(tr))
            
            if i!=max_:
                a.append(tr[i])
                
            else:
                b.append(tr[i])
        #print(a)
        #print(b)
        
        if a[0]**2+a[1]**2 == b[0]**2:
            print('right')
        else:
            print('wrong')
            
