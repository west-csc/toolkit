a=0
num=list(input())
while num != ['6','1','7','4']:
    a+=1
    num = list(str(int(''.join(sorted(num, reverse=True))) - int(''.join(sorted(num)))))
    if len(num)==3:
        num = ["0"]+num
print(a)