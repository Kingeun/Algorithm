#9461
t=int(input())

arr=[1,1,1]
for i in range(3,101):
    arr.append((arr[i-3]+arr[i-2]))
    
#print(arr)
for i in range(t):
    print(arr[(int(input()))-1])
