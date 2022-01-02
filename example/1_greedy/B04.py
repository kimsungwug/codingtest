#2217번 로프
n=int(input())
ropes=[0]*n
for i in range(n):
    ropes[i]=int(input())
ropes.sort()
result = ropes[0]*n
for i in range(n):
    if(ropes[i]>=result):
        result=ropes[i]
    if ropes[i]*(n-i)>=result:
        result=ropes[i]*(n-i)
print(result)
