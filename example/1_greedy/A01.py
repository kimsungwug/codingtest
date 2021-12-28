#모험가 길드
n = int(input())
player=list(map(int,input().split()))
count = 0
result = 0
for i in player:
    count+=1
    if(count>=i):
        count=0
        result+=1
print(result)