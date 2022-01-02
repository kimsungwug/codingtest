#11047 동전 0
count = 0
n,k = map(int, input().split())

coins=[0]*n
for i in range(n):
    coins[i] = int(input())

coins.sort(reverse=True)

for coin_type in coins:
    count+=k//coin_type
    k=k-coin_type*(k//coin_type)
    if(k==0):
        break
print(count)