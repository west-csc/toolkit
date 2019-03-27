import random

total = 200
options = [-total/3, 2*total/3]
results = []
successes = []
for j in range(10000):
    i = 0
    total = 200
    while 10<total<43000:
        i += 1
        total += random.choice(options)
    if total > 43000:
        results += [i]
        successes += [1]
    else:
        successes += [0]
    
print(sum(results)/len(results))
print(sum(successes)/len(successes))