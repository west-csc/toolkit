blah = [int(num) for num in input().split(' ')]
m = blah[0]
n = blah[1]
matrix = [input().split(' ') for i in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
            if (i != 0) and (j == 2 and matrix[i - 1][j] == 1):
                matrix[i-1][j] = 2
            elif(i != n) and (j==2 and matrix[i+1][j] == 1):
                matrix[i+1][j] = 2
            elif(j != 0) and (j == 2 and matrix[i][j-1] == 1):
                matrix[i][j-1] = 2
            elif(j != m) and (j == 2 and matrix[i][j+1]) == 1:
                matrix[i][j+1] = 2
print(matrix)       