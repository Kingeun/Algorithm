s=input()
su=int(s[0])

for i in range(1,len(s)):
    n=int(s[i])
    print(n)
    if su<=1:
        su+=n
        print(su)
        
    else:
        su*=n
        print(su)
        
print(su)  
