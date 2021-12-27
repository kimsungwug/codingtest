#큰수의 법칙
n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
result=0
for i in range(1,m+1):
    if(i%(k+1)==0): result+=data[n-2]
    else: result+=data[n-1]

print(result)
