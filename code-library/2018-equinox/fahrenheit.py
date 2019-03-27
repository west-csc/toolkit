import math
deg = input()
if deg[-1]=="F":
    c=str(math.trunc((float(deg[:len(deg) - 1]) - 32 ) * (5/9))) +"C"
else:
    c=str(math.trunc((float(deg[:len(deg)-1]) * (9/5)) + 32))+"F"
print(c)