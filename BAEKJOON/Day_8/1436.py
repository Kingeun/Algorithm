#1436
n = int(input()) 
series=666
count=0

while True:
    if '666' in str(series):
        count+=1
        #print(series)
    if count == n:
        print(series)
        break
    series+=1  #666이 포함된 수가 나올 때 까지 series를 1씩 증가 시킨다
