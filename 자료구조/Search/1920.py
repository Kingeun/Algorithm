# binary search
N=int(input())
be=list(map(int,input().split()))
be.sort()

M=int(input())
af=list(map(int,input().split()))
  
def binSearch(ary,fData):
  pos=-1
  start=0
  end=len(ary)-1

  while (start<=end):
    mid=(start+end)//2

    if fData==ary[mid]:
      return 1
    elif fData>ary[mid]:
      start=mid+1
    else:
      end=mid-1
  return 0
      

position=[]
for i in af:
  print(binSearch(be,i))
  
