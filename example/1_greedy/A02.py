#곱하기 혹은 더하기
s=str(input())
result=0
for i in range(len(s)):
    if(int(s[i])==0 or result==0):
        result+=int(s[i])
    else:
        result*=int(s[i])
print(result)