#문자열 뒤집기
s=str(input())
count0 = 0
count1 = 0
for i in range(len(s)):
    if(i!=0 and int(s[i])!=int(s[i-1]) and int(s[i])==0):
        count0+=1
    elif(i!=0 and int(s[i])!=int(s[i-1]) and int(s[i])==1):
        count1+=1
    elif(i==0 and int(s[i])==0):
        count0+=1
    elif(i==0 and int(s[i])==1):
        count1+=1
print(min(count1,count0))