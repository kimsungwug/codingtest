#럭키 스트레이트
con = input()
half = int(len(con)/2)
first=0
sec=0
for i in range(half):
    first+=int(con[i]) # 0 1 2
    sec+=int(con[half+i]) # 3 4 5
if(first==sec):
    print("LUCKY")
else:
    print("READY")