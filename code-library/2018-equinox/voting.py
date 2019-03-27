
# INCOMPLETE

n = int(input())
names = [input() for i in range(n)]
num = int(input())
votes = [input().split(' ') for i in range(num)]
totals = [[0, name] for name in names]
def count_votes():
    for vote in votes:
        i = 0
        for name in names:
            totals[i][0] += vote.index(name)
            i += 1
    print(totals)
    return(min(totals)[1])
if max(totals)
print(a)