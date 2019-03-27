a = float(input())
q = float(input())
numbounces = 0
while a > 0.0001:
    a *= q
    numbounces += 1
print(numbounces)