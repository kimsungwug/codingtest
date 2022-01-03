#상하좌우
n = int(input())
move_plan = list(map(str, input().split()))
coord = [1,1]
for i in range(len(move_plan)):
    if(move_plan[i]=='U' and coord[0]!=1):
        coord[0]-=1
    if(move_plan[i]=='D' and coord[0]!=n):
        coord[0]+=1
    if(move_plan[i]=='L' and coord[1]!=1):
        coord[1]-=1
    if(move_plan[i]=='R' and coord[1]!=n):
        coord[1]+=1
print(str(coord[0])+" "+str(coord[1]))