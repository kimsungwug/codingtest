#자물쇠와 열쇠
def checked(x, y, n, m, key, result): #x,y는 0 1 2 3 4 5 까지
    unlock=1
    for u in range(n):
        for r in range(n):
            result[u+x][r+y]+=key[u][r] #u+x는 0 1 2 / 1 2 3 / 2 3 4 / 3 4 5
    for i in range(m):
        for j in range(m):
            if(result[i+n][j+n]!=1):
                unlock=0
                break
    for u in range(n):
        for r in range(n):
            result[u+x][r+y]-=key[u][r] #u+x는 0 1 2 / 1 2 3 / 2 3 4 / 3 4 5
    return unlock

def solution(key, lock):
    n=len(key)
    m=len(lock)
    answer = True
    result = [[0]*(n*2+m) for _ in range(n*2+m)]
    unlock=-1
    real=0
    for i in range(m):
        for j in range(m):
            result[i+n][j+n]=lock[i][j]
    for i in range(4):
        key = list(zip(*key[::-1]))
        #이동 범위
        for x in range(n+m):
            for y in range(n+m): # 0 1 2 3 4 5 
                unlock=checked(x,y,n,m,key,result)
                if(unlock==1):
                    real=1
                if(real==1):
                    break
            if(real==1):
                break
        if(real==1):
            break
    if(real==1):
        print("True")
    else:
        print("False")