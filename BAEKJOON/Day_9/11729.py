#11729
def hanoi_tower(n,start,end,mid):  #함수선언
    if n==1:   #탑의 개수가 1개일떼
        print(start,end)  # 바로 시작에서 끝으로 이동
        return  #함수 탈출
    
    #함수호출
    hanoi_tower(n-1,start,mid,end)  # 가장 큰 원반을 제외한 (n-1)개를 mid 기둥으로 옮긴다.
    # (n-1)개의 원반들의 기준에서 mid 기둥이 end 임 (mid 기둥에 마지막에 위치하기 때문)
    print(start,end) #가장 큰 원반을 end 기둥으로 이동한다
    hanoi_tower(n-1,mid,end,start) #(n-1)개의 원반들이 mid 기둥에 위치해있으므로, mid가 시작점으로 바뀌고 start 가 mid 기둥으로 바뀐다.


n = int(input())
print(2**n-1)  #규칙
