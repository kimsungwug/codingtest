#왕실의 나이트
col=['a','b','c','d','e','f','g','h']
coord = input()
#col.index('a')+1
steps=[(-2,-1),(-1,-2),(2,-1),(-1,2),(-2,1),(1,-2),(2,1),(1,2)]
result=0
for step in steps:
    #열 세로 계산
    move_col=(col.index('a')+1)+step[1]
    move_row=int(coord[1])+step[0]
    if(1<=move_col<=8 and 1<=move_row<=8):
        result+=1
print(result)