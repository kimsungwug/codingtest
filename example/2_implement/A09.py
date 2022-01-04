#문자열 압축
data = input()
result = len(data)
count=0
for step in range(1,len(data)):
    cut=""
    prev = data[0:step]
    count = 1
    for j in range(step,len(data),step):
        if prev == data[j:j+step]:
            count+=1
        else:
            cut += str(count)+prev if count>=2 else prev
            prev=data[j:j+step]
            count=1
    cut+=str(count)+prev if count >= 2 else prev
    result=min(result,len(cut))
print(result)