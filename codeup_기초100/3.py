#6034
num_1,num_2=input().split()
num=print(int(num_1)-int(num_2))

#6035
flo_1,flo_2=input().split()
flo=print(float(flo_1)*float(flo_2))

#6036
st,n=input().split()
print(st*int(n),sep=' ')

#6037
n=int(input())
sen=input()
print(n*sen)

#6038
a,b=map(int,input().split())
print(a**b)

#6039
f1,f2=map(float,input().split())
print(f1**f2)

#6040
a,b=map(int,input().split())
print(a//b)

#6041
a,b=map(int,input().split())
print(a%b)

#6042
#소수점 이하 2자리까지 출력
flo=float(input())
print(format(flo,'.2f'))

#round 사용
round(3.101592,2) #3.1을 출력
print(format(3.101592,'.2f')) #3.10을 출력

#6043
f1,f2=map(float,input().split())
print(format(f1/f2,'.3f'))

#6044
num1,num2=map(int,input().split())
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1//num2)
print(num1%num2)
print(format((num1/num2),'.2f'))

#6045
num1,num2,num3=map(int,input().split())
print(num1+num2+num3,format((num1+num2+num3)/3,'.2f'))

#6048
a,b=map(int,input().split())
print(a<b)

#6049
a,b=map(int,input().split())
print(a==b)

#6050
a,b=map(int,input().split())
print(a<=b)

#6051
a,b=map(int,input().split())
print(a!=b)

#6052
a=int(input())
print(a!=0)

#6053
#입력된 정수의 불 값이 False 이면 True, True 이면 False 를 출력한다.
a = bool(int(input()))
print(not a)
