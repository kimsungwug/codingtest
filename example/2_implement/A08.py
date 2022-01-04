#문자열 재정렬
data = input()
result=""
data_list=[]
sum=0
stringlen=0
for i in range(len(data)):
    if(ord(data[i])<=57 and ord(data[i])>=48):
        sum+=ord(data[i])-48
    else:
        stringlen+=1
        data_list.append(ord(data[i]))
data_list.sort()
for i in range(stringlen):
    result+=chr(data_list[i])
print(result+str(sum))
