#만들 수 없는 금액
n = int(input())
data = list(map(int,input().split()))
data.sort() #1 1 2 3 9
target=1
for i in data:
    if(target<i):
        break
    else:
        target+=i
print(target)

1
2=1+1
4=2+2
7=4+3
16=7+9

1
3=1+2
6=3+3
14=6+8