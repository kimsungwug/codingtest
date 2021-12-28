#무지의 먹방 라이브
import heapq

food_times = list(map(int,input().split()))
k = int(input())
result=-1
q=[]
for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i],i+1))

previous = 0
sum_val=0
length=len(q)
while(q):
    sum_val=(q[0][0]-previous)*length 
    if k>=sum_val:
        k-=sum_val
        previous, _ = heapq.heappop(q)
        length-=1
    else:
        idx=k%length
        q.sort(key=lambda x: x[1])
        result=q[idx][1]
        break
print(result)