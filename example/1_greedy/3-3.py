#숫자카드 게임
n,m = map(int,input().split())
result=0
min_value=0
for i in range(n):
    data=list(map(int,input().split()))
    min_value=min(data)
    if(i!=0 and min_value>result):
        result = min_value
    elif(i==0): 
        result = min_value
print(result)