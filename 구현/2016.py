def solution(a, b):
    answer = ''
    mon=[31,29,31,30,31,30,31,31,30,31,30,31] 
    week=['THU','FRI','SAT','SUN','MON','TUE','WED']
    #which=(sum(mon[a-1]+b))%7
    answer=week[(sum(mon[:a-1])+b)%7]
        
    return answer
