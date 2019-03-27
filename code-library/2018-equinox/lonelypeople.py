lonelypeople = 0
m = int(input())
n = int(input())
rows = [list(input()) for i in range(n)]

for y in range(n):
    for x in range(m):
        a=0
        if rows[y][x]=="1":
            try:
                if rows[y-1][x]!='1':
                    a += 0.25
            except:
                a += 0.25
            try:
                if rows[y+1][x]!='1':
                    a += 0.25
            except:
                a += 0.25
            try:
                if rows[y][x-1]!='1':
                    a += 0.25
            except:
                a += 0.25
            try:
                if rows[y][x+1]!='1':
                    a += 0.25
            except:
                a += 0.25
        if a>=1:
            lonelypeople+=1
print(lonelypeople)