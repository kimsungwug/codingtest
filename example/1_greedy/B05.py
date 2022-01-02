#1931번 회의실 배정
n = int(input())
time = list()
for i in range(n):
    time.append(tuple(map(int, input().split())))
time.sort(key=lambda x:(x[1],x[0]))

end_time=time[0][1]
count=1
for i in range(1,n):
  if time[i][0]>=end_time:
    count+=1
    end_time=time[i][1]
print(count)