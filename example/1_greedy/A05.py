#볼링공 고르기
n,m=map(int,input().split())
weight = list(map(int,input().split()))
count=0
diff = len(weight)-len(set(weight))
for i in range(1,n):
    count+=i
print(count-diff)