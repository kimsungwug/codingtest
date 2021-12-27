#거스름돈
n=1260
coin_types=[500,100,50,10]
count=0
for i in coin_types:
    count += n//i
    n=n%i
print(count)