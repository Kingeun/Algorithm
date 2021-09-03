math_1=[1,2,3,4,5]*2000
math_2=[2, 1, 2, 3, 2, 4, 2, 5]*1250
math_3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

#cnt=[0,0,0]

def solution(answers):
    cnt=[0,0,0]
    for i in range(len(answers)):
        if math_1[i]==answers[i]:
            cnt[0]+=1
        if math_2[i]==answers[i]:
            cnt[1]+=1
        if math_3[i]==answers[i]:
            cnt[2]+=1
        
    #print(cnt)
    sol=[]
    for j in range(len(cnt)):
        if cnt[j]==max(cnt):
            sol.append(j+1)
    return sol
