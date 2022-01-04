#게임 개발
n,m=map(int, input().split())
x,y,direct = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
arr[x][y]=2
count=1
result=0
directs=[[-1,0],[0,1],[1,0],[0,-1]]
while(1):
    for i in range(4):
        if arr[x+directs[direct][0]][y+directs[direct][1]]==0 and 0<=x+directs[direct][0]<=n-1 and 0<=y+directs[direct][1]<=n-1:
            arr[x+directs[direct][0]][y+directs[direct][1]]=2
            count+=1
            x+=directs[direct][0]
            y+=directs[direct][1]
            result=1
            break
        direct=(direct+3)%4
    if(result==0):
        for i in range(4): #2->1
            if(arr[x-directs[direct][0]][y-directs[direct][1]]==1 and 0<=x-directs[direct][0]<=n-1 and 0<=y-directs[direct][1]<=n-1):
                break
            direct=(direct+3)%4
        break
    result=0
    
print(count)
