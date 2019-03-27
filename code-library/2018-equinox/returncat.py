import math
n = int(input())
cat = [int(num) for num in input().split(' ')]
cities = [[int(num) for num in input().split(' ')] for city in range(n)]
dist = [math.sqrt(math.pow((cat[0]-city[0]),2)+math.pow((cat[1]-city[1]),2)) for city in cities]
closest = cities[dist.index(min(dist))]
print(' '.join([str(i) for i in closest]))